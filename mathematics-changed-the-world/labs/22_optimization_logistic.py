"""Unit 09 B: synthetic logistic classification; unrun draft."""

from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path

import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260927)
    parser.add_argument("--epochs", type=int, default=40)
    parser.add_argument("--stress", action="store_true", help="leave one feature badly scaled")
    parser.add_argument("--csv", type=Path, default=Path("unit09-logistic.csv"))
    args = parser.parse_args()
    if args.epochs < 1:
        parser.error("--epochs must be positive")

    rng = np.random.default_rng(args.seed)
    n_train, n_test, dim = 240, 120, 16
    raw = rng.normal(size=(n_train + n_test, dim))
    true_w = rng.normal(size=dim) / np.sqrt(dim)
    label = np.where(raw @ true_w + 0.4 * rng.normal(size=len(raw)) >= 0, 1.0, -1.0)
    if args.stress:
        raw[:, 0] *= 100.0
    train, test = raw[:n_train], raw[n_train:]
    y_train, y_test = label[:n_train], label[n_train:]
    reg = 0.03
    lip = float(np.linalg.norm(train, 2) ** 2 / (4 * n_train) + reg)

    def objective(w: np.ndarray, c: float, x: np.ndarray, y: np.ndarray) -> float:
        return float(np.logaddexp(0.0, -y * (x @ w + c)).mean() + 0.5 * reg * (w @ w))

    def gradient(w: np.ndarray, c: float) -> tuple[np.ndarray, float]:
        margin = y_train * (train @ w + c)
        multiplier = -y_train * np.exp(-np.logaddexp(0.0, margin))
        return train.T @ multiplier / n_train + reg * w, float(multiplier.mean())

    rows: list[dict[str, object]] = []
    for method in ("full_gradient", "SGD"):
        w, c = np.zeros(dim), 0.0
        started = time.perf_counter()
        for epoch in range(1, args.epochs + 1):
            if method == "full_gradient":
                dw, dc = gradient(w, c)
                w -= dw / lip
                c -= dc / lip
                gradients_used = n_train
            else:
                for i in rng.permutation(n_train):
                    margin = y_train[i] * (train[i] @ w + c)
                    scalar = -y_train[i] * float(np.exp(-np.logaddexp(0.0, margin)))
                    rate = 0.2 / np.sqrt(epoch * n_train)
                    w -= rate * (scalar * train[i] + reg * w)
                    c -= rate * scalar
                gradients_used = epoch * n_train
            dw, dc = gradient(w, c)
            prediction = np.where(test @ w + c >= 0, 1.0, -1.0)
            rows.append({"method": method, "epoch": epoch,
                         "train_objective": objective(w, c, train, y_train),
                         "test_objective": objective(w, c, test, y_test),
                         "test_accuracy": float(np.mean(prediction == y_test)),
                         "full_gradient_norm": float(np.sqrt(dw @ dw + dc * dc)),
                         "sample_gradients_used": gradients_used if method == "SGD" else epoch * gradients_used,
                         "seconds": time.perf_counter() - started, "stress": args.stress})

    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} unreviewed observations to {args.csv}")


if __name__ == "__main__":
    main()
