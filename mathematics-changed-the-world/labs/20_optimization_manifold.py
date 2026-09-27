"""Unit 08 sphere and Stiefel Rayleigh models; not yet run or validated."""

from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path

import numpy as np


def qr_retraction(candidate: np.ndarray) -> np.ndarray:
    """Thin QR with column-sign correction, so R_X(0)=X for orthonormal X."""
    q, r = np.linalg.qr(candidate, mode="reduced")
    signs = np.where(np.diag(r) < 0.0, -1.0, 1.0)
    return q * signs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260927)
    parser.add_argument("--iterations", type=int, default=120)
    parser.add_argument("--csv", type=Path, default=Path("unit08-history.csv"))
    args = parser.parse_args()
    if args.iterations < 1:
        parser.error("--iterations must be positive")

    rng = np.random.default_rng(args.seed)
    q, _ = np.linalg.qr(rng.normal(size=(8, 8)))
    eigenvalues = np.linspace(0.5, 8.0, 8)
    matrix = (q * eigenvalues) @ q.T
    rows: list[dict[str, object]] = []

    for start_name, x0 in (("random", rng.normal(size=8)), ("largest_eigenvector", q[:, -1])):
        x = x0 / np.linalg.norm(x0)
        started = time.perf_counter()
        for k in range(args.iterations + 1):
            value = float(x @ matrix @ x)
            tangent_gradient = 2 * (matrix @ x - value * x)
            rows.append({"model": "sphere", "start": start_name, "iteration": k,
                         "objective": value, "reference_minimum": float(eigenvalues[0]),
                         "tangent_gradient_norm": float(np.linalg.norm(tangent_gradient)),
                         "constraint_error": abs(float(x @ x) - 1.0),
                         "subspace_error": "",
                         "seconds": time.perf_counter() - started})
            if k == args.iterations:
                break
            candidate = x - 0.08 * tangent_gradient
            x = candidate / np.linalg.norm(candidate)  # sphere retraction

    p = 2
    target_projector = q[:, :p] @ q[:, :p].T
    for start_name, x0 in (("random", rng.normal(size=(8, p))),
                           ("largest_eigenspace", q[:, -p:])):
        x = qr_retraction(x0)
        started = time.perf_counter()
        for k in range(args.iterations + 1):
            ax = matrix @ x
            value = float(np.trace(x.T @ ax))
            euclidean_gradient = 2 * ax
            sym = 0.5 * (x.T @ euclidean_gradient + euclidean_gradient.T @ x)
            tangent_gradient = euclidean_gradient - x @ sym
            rows.append({"model": "stiefel", "start": start_name, "iteration": k,
                         "objective": value, "reference_minimum": float(eigenvalues[:p].sum()),
                         "tangent_gradient_norm": float(np.linalg.norm(tangent_gradient)),
                         "constraint_error": float(np.linalg.norm(x.T @ x - np.eye(p))),
                         "subspace_error": float(np.linalg.norm(x @ x.T - target_projector)),
                         "seconds": time.perf_counter() - started})
            if k == args.iterations:
                break
            x = qr_retraction(x - 0.04 * tangent_gradient)

    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} unreviewed teaching observations to {args.csv}")


if __name__ == "__main__":
    main()
