#!/usr/bin/env python3
"""Search committed Math Atlas chapters and existing resource links offline."""
from __future__ import annotations

import argparse
import io
import json
import re
import subprocess
import sys
import tarfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

ALIASES = {
    "傅里叶": ["傅里叶", "fourier"],
    "傅里叶变换": ["傅里叶", "fourier"],
    "fourier": ["fourier", "傅里叶"],
    "拉普拉斯": ["拉普拉斯", "laplace"],
    "laplace": ["laplace", "拉普拉斯"],
    "z变换": ["z变换", "z 变换", "z-transform", "z transform"],
    "牛顿法": ["牛顿法", "newton"],
    "贝叶斯": ["贝叶斯", "bayes", "bayesian"],
    "bayes": ["bayes", "bayesian", "贝叶斯"],
    "微积分": ["微积分", "calculus"],
    "线性代数": ["线性代数", "linear algebra"],
    "凸优化": ["凸优化", "convex optimization"],
    "流形": ["流形", "manifold", "riemannian"],
    "随机梯度": ["随机梯度", "stochastic gradient", "sgd"],
    "sgd": ["sgd", "stochastic gradient", "随机梯度"],
    "文再文": ["文再文", "wenzw", "optbook"],
}


def git(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=repo)


def split_sections(text: str) -> tuple[str, list[dict]]:
    lines = text.splitlines()
    title = "Untitled"
    sections, start, heading, hierarchy, fence = [], 1, "文档开头", [], None
    for number, line in enumerate(lines, 1):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[marker.end():].strip():
                fence = None
            continue
        match = None if fence else re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if match:
            if number > start:
                sections.append({"heading": heading, "line": start, "end": number - 1, "text": "\n".join(lines[start - 1:number - 1])})
            level, label = len(match.group(1)), match.group(2)
            if level == 1 and title == "Untitled":
                title = label
            hierarchy = [(depth, name) for depth, name in hierarchy if depth < level]
            hierarchy.append((level, label))
            heading = " › ".join(name for depth, name in hierarchy if depth > 1) or label
            start = number
    if lines:
        sections.append({"heading": heading, "line": start, "end": len(lines), "text": "\n".join(lines[start - 1:])})
    return title, sections


def resource_links(text: str) -> list[dict]:
    """Expose existing HTTP(S) references as inert labels, never fetch them."""
    links, seen = [], set()
    labelled = {url: label for label, url in re.findall(r"\[([^\]\n]+)\]\((https?://[^\s)]+)\)", text)}
    for match in re.finditer(r"https?://[^\s<>`\"]+", text):
        url = match.group().rstrip(".,;:，。；：")
        while url.endswith(")") and url.count(")") > url.count("("):
            url = url[:-1]
        if url not in seen:
            seen.add(url)
            links.append({"label": labelled.get(url, url), "url": url})
    return links


def classify(path: str) -> tuple[str, str]:
    if "/docs/core/" in path:
        return "九个核心专题", "数学专题"
    if "/docs/branches/" in path:
        return "数学主干", "数学专题"
    if "/docs/bridges/" in path:
        return "专题桥梁", "跨主题教程"
    if "/docs/courses/" in path:
        return "最优化课程", "课程与讲义"
    if "/labs/" in path:
        return "实验与运行记录", "实验资料"
    if "references" in path.lower() or "coverage-matrix" in path:
        return "参考资料与覆盖记录", "资料索引"
    if "/docs/" in path:
        return "学习导航", "导航页面"
    return "项目说明与历史", "项目说明"


def build_index(repo: Path, revision: str = "HEAD", repository: str = "Jaycob-jh/math-atlas") -> dict:
    commit = git(repo, "rev-parse", revision).decode().strip()
    documents = []
    # Read committed data without extracting files or indexing ignored/private local data.
    with tarfile.open(fileobj=io.BytesIO(git(repo, "archive", commit))) as archive:
        for member in archive:
            if not member.isfile() or not member.name.endswith(".md"):
                continue
            if member.name.startswith(".github/"):
                continue
            source = archive.extractfile(member)
            text = source.read().decode("utf-8-sig")
            title, sections = split_sections(text)
            # Bare title/comment blocks provide no explanatory passage to preview.
            sections = [s for s in sections if re.sub(r"^#{1,6}\s+.*$", "", re.sub(r"<!--.*?-->", "", s["text"], flags=re.S), flags=re.M).strip()]
            for section in sections:
                section["resources"] = resource_links(section["text"])
            path = member.name
            module, role = classify(path)
            documents.append({"path": path, "module": module, "role": role, "title": title, "sections": sections,
                              "url": f"https://github.com/{repository}/blob/{commit}/{quote(path, safe='/')}"})
    return {"commit": commit, "built_at": datetime.now(timezone.utc).isoformat(), "documents": documents, "aliases": ALIASES}


def query_terms(query: str, expand: bool = True) -> list[str]:
    value = query.strip().lower()
    return ALIASES.get(value, [value]) if expand else [value]


def count_term(text: str, term: str) -> int:
    if re.fullmatch(r"[a-z0-9_]+", term):
        return len(re.findall(r"(?<![a-z0-9_])" + re.escape(term) + r"(?![a-z0-9_])", text.lower()))
    return text.lower().count(term)


def search(index: dict, query: str, module: str = "", expand: bool = True) -> list[dict]:
    terms = query_terms(query, expand)
    if not query.strip():
        return []
    found = []
    for document in index["documents"]:
        if module and document["module"] != module:
            continue
        hits = []
        for section in document["sections"]:
            score = sum(30 * min(count_term(section["heading"], t), 3) + min(count_term(section["text"], t), 10) for t in terms)
            if score:
                score += sum(40 * min(count_term(document["title"], t), 2) for t in terms)
                score += 8 if document["role"] == "数学专题" else 0
                hits.append({**section, "score": score, "url": document["url"] + f'#L{section["line"]}'})
        if hits:
            hits.sort(key=lambda s: (-s["score"], s["line"]))
            found.append({k: v for k, v in document.items() if k != "sections"} | {"score": hits[0]["score"], "hits": hits})
    return sorted(found, key=lambda d: (-d["score"], d["path"]))


def write_page(index: dict, template: Path, output: Path) -> None:
    # Escape script termination even when source Markdown contains malicious HTML.
    payload = json.dumps(index, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    page = template.read_text(encoding="utf-8").replace("/*__KNOWLEDGE_INDEX__*/", "const INDEX = " + payload + ";")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(page, encoding="utf-8")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--revision", default="HEAD")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--query")
    parser.add_argument("--module", default="")
    parser.add_argument("--exact", action="store_true", help="Disable explicitly configured related-term expansion")
    args = parser.parse_args()
    index = build_index(args.repo, args.revision)
    if args.query is not None:
        print(json.dumps({"query": args.query, "terms": query_terms(args.query, not args.exact), "commit": index["commit"], "results": search(index, args.query, args.module, not args.exact)}, ensure_ascii=False, indent=2))
    else:
        output = args.output or args.repo / "mathematics-changed-the-world/docs/knowledge-search/index.html"
        write_page(index, args.repo / "scripts/math_search_template.html", output)
        print(json.dumps({"output": str(output.resolve()), "commit": index["commit"], "documents": len(index["documents"]), "sections": sum(len(d["sections"]) for d in index["documents"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
