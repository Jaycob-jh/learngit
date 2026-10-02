# 关键词资料检索

[打开数学资料检索页](knowledge-search/index.html)，输入“傅里叶变换”“凸优化”“流形”“Bayes”或“文再文”，即可定位资料所在的文件和章节。页面支持资料分类、中英相关词、章节预览及原章节的教材/课程链接；Ctrl+K回到搜索框。

## GitHub与离线使用

GitHub普通文件页显示HTML源码。打开[检索文件](https://github.com/Jaycob-jh/math-atlas/blob/math-changed-world/mathematics-changed-the-world/docs/knowledge-search/index.html)，选择Download raw file下载后双击，无需Python、服务或API key。也可把同一个HTML文件交给共创者。

检索在本机完成；打开GitHub原文或教材、课程、PDF外链需要联网。每条命中定位到构建索引时的固定Git提交及源行号，资料更新后需重新下载生成的HTML。

## 检索范围

索引覆盖构建提交中的Markdown，包括九个核心专题、数学主干、专题桥梁、最优化课程、学习导航、参考资料及实验记录。它检索已有章节文字和链接，不下载外链PDF正文，不对扫描教材进行OCR，也不代表资料已经全部审读或代码已经运行。相关词用于发现资料，不表示方法或概念等价。

## 维护

先提交资料修改，再从该提交生成索引，保证预览与原文一致：

```bash
python scripts/math_search.py
python scripts/math_search.py --query "傅里叶变换"
python scripts/math_search.py --query "凸优化" --module "最优化课程"
python -m unittest discover -s scripts/tests -v
```

只读取Git已提交资料；本地未提交笔记不会自动进入可分享快照。生成器仅需Python标准库。可用`--revision`选择已存在的提交，或用`--exact`关闭相关词扩展。
