"""Unit 06: compare four solvers on one convex LASSO problem.

All methods solve 0.5 * ||Ax-b||_2**2 + lam * ||x||_1. The fixed seed and
common stopping diagnostic make mechanisms comparable, not a speed ranking.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np


def soft_threshold(v: np.ndarray, threshold: float) -> np.ndarray:
    return np.sign(v) * np.maximum(np.abs(v) - threshold, 0.0)


def objective(a: np.ndarray, b: np.ndarray, x: np.ndarray, lam: float) -> float:
    return float(0.5 * np.linalg.norm(a @ x - b) ** 2 + lam * np.linalg.norm(x, 1))


def prox_gradient_residual(
    a: np.ndarray, b: np.ndarray, x: np.ndarray, lam: float, step: float
) -> float:
    """Norm of the proximal gradient mapping; zero iff convex KKT holds."""
    gradient = a.T @ (a @ x - b)
    prox = soft_threshold(x - step * gradient, step * lam)
    return float(np.linalg.norm(x - prox) / step)


def make_problem(seed: int = 18) -> tuple[np.ndarray, np.ndarray, float]:
    rng = np.random.default_rng(seed)
    m, n = 80, 24
    a = rng.normal(size=(m, n))
    a[:, 1] = 0.8 * a[:, 0] + 0.2 * a[:, 1]
    a /= np.linalg.norm(a, axis=0)
    true_x = np.zeros(n)
    true_x[[0, 3, 8, 17]] = [1.8, -1.4, 1.1, -0.9]
    b = a @ true_x + 0.04 * rng.normal(size=m)
    return a, b, 0.12


def ista(
    a: np.ndarray, b: np.ndarray, lam: float, iterations: int, step: float
) -> list[tuple[np.ndarray, float, float, float, float]]:
    x = np.zeros(a.shape[1])
    history = []
    for _ in range(iterations):
        x = soft_threshold(x - step * (a.T @ (a @ x - b)), step * lam)
        history.append((x.copy(), objective(a, b, x, lam),
                        prox_gradient_residual(a, b, x, lam, step), 0.0, 0.0))
    return history


def fista(
    a: np.ndarray, b: np.ndarray, lam: float, iterations: int, step: float
) -> list[tuple[np.ndarray, float, float, float, float]]:
    x = np.zeros(a.shape[1])
    y = x.copy()
    t = 1.0
    history = []
    for _ in range(iterations):
        x_next = soft_threshold(y - step * (a.T @ (a @ y - b)), step * lam)
        t_next = (1.0 + np.sqrt(1.0 + 4.0 * t * t)) / 2.0
        y = x_next + ((t - 1.0) / t_next) * (x_next - x)
        x, t = x_next, t_next
        history.append((x.copy(), objective(a, b, x, lam),
                        prox_gradient_residual(a, b, x, lam, step), 0.0, 0.0))
    return history


def coordinate_descent(
    a: np.ndarray, b: np.ndarray, lam: float, epochs: int, step: float
) -> list[tuple[np.ndarray, float, float, float, float]]:
    x = np.zeros(a.shape[1])
    residual = -b.copy()  # Ax-b; kept in sync after each coordinate update.
    column_norms = np.sum(a * a, axis=0)
    if np.any(column_norms <= 0):
        raise ValueError("Coordinate descent requires nonzero columns")
    history = []
    for _ in range(epochs):
        for j in range(a.shape[1]):
            old = x[j]
            x[j] = soft_threshold(
                np.asarray(old - a[:, j] @ residual / column_norms[j]),
                lam / column_norms[j],
            ).item()
            residual += a[:, j] * (x[j] - old)
        history.append((x.copy(), objective(a, b, x, lam),
                        prox_gradient_residual(a, b, x, lam, step), 0.0, 0.0))
    return history


def admm(
    a: np.ndarray, b: np.ndarray, lam: float, iterations: int,
    step: float, rho: float = 1.0,
) -> list[tuple[np.ndarray, float, float, float, float]]:
    if rho <= 0:
        raise ValueError("rho must be positive")
    n = a.shape[1]
    gram = a.T @ a
    rhs_data = a.T @ b
    # The positive rho term makes the x subproblem nonsingular.
    factor = np.linalg.cholesky(gram + rho * np.eye(n))
    x = np.zeros(n)
    z = np.zeros(n)
    u = np.zeros(n)
    history = []
    for _ in range(iterations):
        rhs = rhs_data + rho * (z - u)
        x = np.linalg.solve(factor.T, np.linalg.solve(factor, rhs))
        old_z = z.copy()
        z = soft_threshold(x + u, lam / rho)
        u += x - z
        primal = float(np.linalg.norm(x - z))
        dual = float(rho * np.linalg.norm(z - old_z))
        # z is reported as the sparse candidate; its objective is not the
        # split augmented-Lagrangian objective while x != z.
        history.append((z.copy(), objective(a, b, z, lam),
                        prox_gradient_residual(a, b, z, lam, step), primal, dual))
    return history


def write_history(path: Path, histories: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["method", "iteration_or_epoch", "objective",
                         "prox_gradient_residual", "primal_residual", "dual_residual"])
        for method, records in histories.items():
            for index, (_, value, pg, primal, dual) in enumerate(records, 1):
                writer.writerow([method, index, value, pg, primal, dual])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--iterations", type=int, default=250)
    parser.add_argument("--csv", type=Path, help="Optional path for iteration diagnostics")
    args = parser.parse_args()
    if args.iterations <= 0:
        parser.error("--iterations must be positive")

    a, b, lam = make_problem()
    lipschitz = float(np.linalg.norm(a, 2) ** 2)
    step = 1.0 / lipschitz
    histories = {
        "ISTA": ista(a, b, lam, args.iterations, step),
        "FISTA": fista(a, b, lam, args.iterations, step),
        "cyclic-CD": coordinate_descent(a, b, lam, args.iterations, step),
        "ADMM": admm(a, b, lam, args.iterations, step),
    }
    print(f"LASSO: m={a.shape[0]}, n={a.shape[1]}, lambda={lam}, L={lipschitz:.6f}")
    print("method       objective      prox-grad      primal        dual")
    for method, records in histories.items():
        _, value, pg, primal, dual = records[-1]
        print(f"{method:10s} {value:12.8f} {pg:12.3e} {primal:12.3e} {dual:12.3e}")
    # Counterexample: a gradient step larger than 2/L on a scalar quadratic.
    scalar = 1.0
    for _ in range(8):
        scalar -= 2.2 * scalar
    print(f"failure case: f(x)=x^2/2, step=2.2>2/L, |x_8|={abs(scalar):.6f}")
    if args.csv:
        write_history(args.csv, histories)
        print(f"diagnostics: {args.csv}")


if __name__ == "__main__":
    main()
