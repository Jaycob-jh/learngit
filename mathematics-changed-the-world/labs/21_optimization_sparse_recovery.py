"""Unit 09 A: synthetic sparse recovery with ISTA and FISTA."""

from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path

import numpy as np


def threshold(x: np.ndarray, amount: float) -> np.ndarray:
    return np.sign(x) * np.maximum(np.abs(x) - amount, 0.0)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260927)
    parser.add_argument("--iterations", type=int, default=250)
    parser.add_argument("--lambda-value", type=float, default=0.002)
    parser.add_argument("--stress", action="store_true", help="make two columns nearly collinear")
    parser.add_argument("--csv", type=Path, default=Path("unit09-sparse.csv"))
    args = parser.parse_args()
    if args.iterations < 1:
        parser.error("--iterations must be positive")
    if args.lambda_value < 0:
        parser.error("--lambda-value must be nonnegative")

    rng = np.random.default_rng(args.seed)
    m, n = 48, 96
    a = rng.normal(size=(m, n))
    noise = 0.03 * rng.normal(size=m)
    if args.stress:
        # A separate stream keeps the observation noise identical across modes.
        jitter_rng = np.random.default_rng(args.seed + 1)
        a[:, 1] = a[:, 0] + 0.01 * jitter_rng.normal(size=m)
    a /= np.linalg.norm(a, axis=0, keepdims=True)
    truth = np.zeros(n)
    truth[[0, 1, 7, 18, 46]] = [1.5, -0.8, 1.1, -1.2, 0.9]
    b = a @ truth + noise
    lam = args.lambda_value
    lip = float(np.linalg.norm(a, 2) ** 2 / m)
    step = 1 / lip

    def grad(x: np.ndarray) -> np.ndarray:
        return a.T @ (a @ x - b) / m

    def objective(x: np.ndarray) -> float:
        return float(0.5 * np.linalg.norm(a @ x - b) ** 2 / m + lam * np.abs(x).sum())

    rows: list[dict[str, object]] = []
    for method in ("ISTA", "FISTA"):
        x = np.zeros(n)
        y = x.copy()
        momentum = 1.0
        started = time.perf_counter()
        for k in range(1, args.iterations + 1):
            old = x.copy()
            x = threshold(y - step * grad(y), step * lam)
            if method == "FISTA":
                next_momentum = (1 + np.sqrt(1 + 4 * momentum**2)) / 2
                y = x + ((momentum - 1) / next_momentum) * (x - old)
                momentum = next_momentum
            else:
                y = x.copy()
            mapping = (x - threshold(x - step * grad(x), step * lam)) / step
            predicted = set(np.flatnonzero(np.abs(x) > 0.05).tolist())
            actual = set(np.flatnonzero(truth).tolist())
            rows.append({"method": method, "iteration": k, "objective": objective(x),
                         "prox_mapping_norm": float(np.linalg.norm(mapping)),
                         "relative_recovery_error": float(np.linalg.norm(x - truth) / np.linalg.norm(truth)),
                         "support_symmetric_difference": len(predicted ^ actual),
                         "seconds": time.perf_counter() - started, "stress": args.stress,
                         "lambda_value": lam})

    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} unreviewed observations to {args.csv}")


if __name__ == "__main__":
    main()
