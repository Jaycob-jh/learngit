"""Optimization modeling lab: loss choice and regularization structure.

This experiment supports PKU optimization study Unit 02.
The goal is to observe how modeling choices change the solution.
The numerical solvers are intentionally simple; algorithmic convergence
is studied in later units.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


def fit_ordinary_least_squares(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Solve min_x ||Ax-b||_2^2."""
    x, *_ = np.linalg.lstsq(a, b, rcond=None)
    return x


def fit_least_absolute_deviations(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Solve min_x ||Ax-b||_1 through a linear-program epigraph form."""
    m, n = a.shape
    objective = np.concatenate([np.zeros(n), np.ones(m)])

    # Residual r = Ax-b. Enforce -u <= r <= u and u >= 0.
    a_ub = np.block(
        [
            [a, -np.eye(m)],
            [-a, -np.eye(m)],
        ]
    )
    b_ub = np.concatenate([b, -b])
    bounds = [(None, None)] * n + [(0.0, None)] * m

    result = linprog(
        objective,
        A_ub=a_ub,
        b_ub=b_ub,
        bounds=bounds,
        method="highs",
    )
    if not result.success:
        raise RuntimeError(f"LAD linear program failed: {result.message}")
    return result.x[:n]


def soft_threshold(z: np.ndarray, threshold: float) -> np.ndarray:
    return np.sign(z) * np.maximum(np.abs(z) - threshold, 0.0)


def fit_lasso_ista(
    a: np.ndarray,
    b: np.ndarray,
    *,
    lam: float = 0.15,
    steps: int = 3000,
) -> np.ndarray:
    """Approximately solve 0.5||Ax-b||_2^2 + lam||x||_1 with ISTA."""
    lipschitz = np.linalg.norm(a, 2) ** 2
    step_size = 1.0 / lipschitz
    x = np.zeros(a.shape[1])

    for _ in range(steps):
        gradient = a.T @ (a @ x - b)
        x = soft_threshold(x - step_size * gradient, lam * step_size)

    return x


def regression_with_outliers_demo() -> None:
    """Compare L2 and L1 residual models on the same contaminated data."""
    rng = np.random.default_rng(7)
    t = np.linspace(-2.0, 2.0, 60)
    a = np.column_stack([t, np.ones_like(t)])
    true_beta = np.array([2.0, -0.5])

    clean = a @ true_beta + 0.15 * rng.normal(size=t.size)
    observed = clean.copy()
    outliers = np.array([5, 18, 47])
    observed[outliers] += np.array([5.0, -6.0, 7.0])

    ols = fit_ordinary_least_squares(a, observed)
    lad = fit_least_absolute_deviations(a, observed)

    print("Regression with outliers")
    print("true beta:", true_beta)
    print("least-squares beta:", np.round(ols, 4))
    print("least-absolute-deviations beta:", np.round(lad, 4))
    print(
        "median absolute residual (LS / LAD):",
        round(float(np.median(np.abs(a @ ols - observed))), 4),
        "/",
        round(float(np.median(np.abs(a @ lad - observed))), 4),
    )

    grid = np.linspace(t.min(), t.max(), 200)
    design = np.column_stack([grid, np.ones_like(grid)])

    plt.figure(figsize=(8, 5))
    plt.scatter(t, observed, label="observed data")
    plt.plot(grid, design @ ols, label="least squares")
    plt.plot(grid, design @ lad, label="least absolute deviations")
    plt.xlabel("t")
    plt.ylabel("response")
    plt.title("Same data, different residual models")
    plt.legend()
    plt.tight_layout()
    plt.show()


def sparse_regularization_demo() -> None:
    """Compare L2 and L1 regularization on a sparse linear model."""
    rng = np.random.default_rng(12)
    m, n = 80, 20
    a = rng.normal(size=(m, n))
    a = a / np.linalg.norm(a, axis=0)

    true_x = np.zeros(n)
    true_x[[1, 5, 11, 17]] = np.array([1.5, -2.2, 0.9, 1.8])
    b = a @ true_x + 0.05 * rng.normal(size=m)

    ridge_lambda = 0.2
    ridge = np.linalg.solve(
        a.T @ a + ridge_lambda * np.eye(n),
        a.T @ b,
    )
    lasso = fit_lasso_ista(a, b, lam=0.15)

    ridge_active = int(np.count_nonzero(np.abs(ridge) > 1e-3))
    lasso_active = int(np.count_nonzero(np.abs(lasso) > 1e-3))

    print("\nSparse regularization")
    print("true nonzero coefficients:", int(np.count_nonzero(true_x)))
    print("ridge coefficients above 1e-3:", ridge_active)
    print("LASSO coefficients above 1e-3:", lasso_active)

    index = np.arange(n)
    plt.figure(figsize=(9, 5))
    plt.plot(index, true_x, "o-", label="true coefficients")
    plt.plot(index, ridge, "o-", label="ridge")
    plt.plot(index, lasso, "o-", label="LASSO")
    plt.xlabel("coefficient index")
    plt.ylabel("coefficient value")
    plt.title("Regularizer choice changes the recovered structure")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main() -> None:
    regression_with_outliers_demo()
    sparse_regularization_demo()


if __name__ == "__main__":
    main()
