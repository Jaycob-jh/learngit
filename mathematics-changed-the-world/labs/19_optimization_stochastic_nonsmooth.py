"""Unit 07 teaching experiment; source-level and numerical review pending.

Compares subgradient/proximal gradient on LASSO, then full gradient/SGD/SVRG
on one finite-sum logistic model. Outputs raw per-iteration metrics as CSV.
No result is claimed by this file until it is actually run and inspected.
"""

from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path

import numpy as np


def soft_threshold(x: np.ndarray, threshold: float) -> np.ndarray:
    return np.sign(x) * np.maximum(np.abs(x) - threshold, 0.0)


def sigmoid_neg(z: np.ndarray) -> np.ndarray:
    return np.exp(-np.logaddexp(0.0, z))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260927)
    parser.add_argument("--iterations", type=int, default=120)
    parser.add_argument("--csv", type=Path, default=Path("unit07-history.csv"))
    args = parser.parse_args()
    if args.iterations < 1:
        parser.error("--iterations must be positive")

    rng = np.random.default_rng(args.seed)
    rows: list[dict[str, object]] = []
    a = rng.normal(size=(80, 24)) / np.sqrt(80)
    truth = np.zeros(24)
    truth[:4] = [1.5, -1.0, 0.8, -0.5]
    b = a @ truth + 0.03 * rng.normal(size=80)
    lam = 0.08
    lip = float(np.linalg.norm(a, 2) ** 2)

    def lasso_objective(x: np.ndarray) -> float:
        return float(0.5 * np.linalg.norm(a @ x - b) ** 2 + lam * np.abs(x).sum())

    for method in ("subgradient", "proximal_gradient"):
        x = np.zeros(24)
        started = time.perf_counter()
        for k in range(1, args.iterations + 1):
            grad = a.T @ (a @ x - b)
            if method == "subgradient":
                # Zero is one valid subgradient of |x| at x=0.
                x -= (0.4 / np.sqrt(k)) * (grad + lam * np.sign(x))
            else:
                x = soft_threshold(x - grad / lip, lam / lip)
            mapping = lip * (x - soft_threshold(x - (a.T @ (a @ x - b)) / lip, lam / lip))
            rows.append({"problem": "lasso", "method": method, "step": k,
                         "objective": lasso_objective(x), "metric": float(np.linalg.norm(mapping)),
                         "metric_name": "proximal_gradient_mapping", "seconds": time.perf_counter() - started})

    n, dim = 180, 12
    data = rng.normal(size=(n, dim))
    weights = rng.normal(size=dim) / np.sqrt(dim)
    labels = np.where(data @ weights + 0.3 * rng.normal(size=n) >= 0, 1.0, -1.0)
    reg = 0.03
    lip_logistic = float(np.linalg.norm(data, 2) ** 2 / (4 * n) + reg)

    def sample_gradient(x: np.ndarray, i: int) -> np.ndarray:
        margin = labels[i] * float(data[i] @ x)
        return -labels[i] * data[i] * float(sigmoid_neg(np.array(margin))) + reg * x

    def full_gradient(x: np.ndarray) -> np.ndarray:
        margin = labels * (data @ x)
        return -(data.T @ (labels * sigmoid_neg(margin))) / n + reg * x

    def logistic_objective(x: np.ndarray) -> float:
        return float(np.logaddexp(0.0, -labels * (data @ x)).mean() + 0.5 * reg * (x @ x))

    for method in ("full_gradient", "sgd", "svrg"):
        x = np.zeros(dim)
        snapshot = x.copy()
        snapshot_grad = full_gradient(snapshot)
        started = time.perf_counter()
        for k in range(1, args.iterations + 1):
            if method == "full_gradient":
                direction = full_gradient(x)
                step = 1 / lip_logistic
            elif method == "sgd":
                direction = sample_gradient(x, int(rng.integers(n)))
                step = 0.2 / np.sqrt(k)
            else:
                if (k - 1) % n == 0:
                    snapshot = x.copy()
                    snapshot_grad = full_gradient(snapshot)
                i = int(rng.integers(n))
                direction = sample_gradient(x, i) - sample_gradient(snapshot, i) + snapshot_grad
                step = 0.1 / lip_logistic
            x -= step * direction
            rows.append({"problem": "logistic", "method": method, "step": k,
                         "objective": logistic_objective(x), "metric": float(np.linalg.norm(full_gradient(x))),
                         "metric_name": "full_gradient_norm", "seconds": time.perf_counter() - started})

    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} unreviewed teaching observations to {args.csv}")


if __name__ == "__main__":
    main()
