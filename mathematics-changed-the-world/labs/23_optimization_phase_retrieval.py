"""Unit 09 C: real-valued phase retrieval on synthetic data."""

from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path

import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260927)
    parser.add_argument("--iterations", type=int, default=250)
    parser.add_argument("--stress", action="store_true", help="fewer, noisier measurements")
    parser.add_argument("--csv", type=Path, default=Path("unit09-phase.csv"))
    args = parser.parse_args()
    if args.iterations < 1:
        parser.error("--iterations must be positive")

    rng = np.random.default_rng(args.seed)
    dim = 12
    sample_count = 24 if args.stress else 240
    a = rng.normal(size=(sample_count, dim))
    truth = rng.normal(size=dim)
    truth /= np.linalg.norm(truth)
    noise_sd = 0.3 if args.stress else 0.02
    observed = (a @ truth) ** 2 + noise_sd * rng.normal(size=sample_count)
    spectral_matrix = a.T @ (observed[:, None] * a) / sample_count
    _, eigenvectors = np.linalg.eigh(spectral_matrix)
    spectral = eigenvectors[:, -1] * np.sqrt(max(float(observed.mean()), 1e-12))
    random_start = rng.normal(size=dim)
    random_start /= np.linalg.norm(random_start)
    random_start *= np.linalg.norm(spectral)

    def objective(x: np.ndarray) -> float:
        residual = (a @ x) ** 2 - observed
        return float(residual @ residual / (4 * sample_count))

    def gradient(x: np.ndarray) -> np.ndarray:
        projected = a @ x
        return a.T @ (((projected**2) - observed) * projected) / sample_count

    rows: list[dict[str, object]] = []
    for start_name, x0 in (("spectral", spectral), ("random", random_start)):
        x = x0.copy()
        started = time.perf_counter()
        for k in range(args.iterations + 1):
            grad = gradient(x)
            sign_error = min(np.linalg.norm(x - truth), np.linalg.norm(x + truth))
            rows.append({"start": start_name, "iteration": k, "objective": objective(x),
                         "gradient_norm": float(np.linalg.norm(grad)),
                         "sign_invariant_error": float(sign_error / np.linalg.norm(truth)),
                         "observation_rmse": float(np.sqrt(np.mean(((a @ x) ** 2 - observed) ** 2))),
                         "seconds": time.perf_counter() - started, "stress": args.stress})
            if k == args.iterations:
                break
            step = 0.1
            current = objective(x)
            while step > 1e-10 and objective(x - step * grad) > current - 1e-4 * step * float(grad @ grad):
                step *= 0.5
            if step <= 1e-10:
                break
            x -= step * grad

    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} unreviewed observations to {args.csv}")


if __name__ == "__main__":
    main()
