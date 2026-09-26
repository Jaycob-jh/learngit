"""Optimization lab: convexity checks and conditioning effects.

This experiment supports the PKU optimization study Unit 01.
It is a numerical illustration, not a proof of convexity or convergence.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def quadratic_value(x: np.ndarray, q: np.ndarray, b: np.ndarray) -> float:
    return float(0.5 * x @ q @ x + b @ x)


def convexity_violations(
    q: np.ndarray,
    b: np.ndarray,
    *,
    trials: int = 5000,
    seed: int = 7,
    tol: float = 1e-12,
) -> int:
    """Count sampled violations of the convexity inequality."""
    rng = np.random.default_rng(seed)
    violations = 0

    for _ in range(trials):
        x = rng.normal(size=q.shape[0])
        y = rng.normal(size=q.shape[0])
        theta = rng.uniform()

        lhs = quadratic_value(theta * x + (1.0 - theta) * y, q, b)
        rhs = (
            theta * quadratic_value(x, q, b)
            + (1.0 - theta) * quadratic_value(y, q, b)
        )
        if lhs > rhs + tol:
            violations += 1

    return violations


def gradient_descent_quadratic(
    q: np.ndarray,
    b: np.ndarray,
    x0: np.ndarray,
    *,
    steps: int = 120,
) -> tuple[np.ndarray, np.ndarray]:
    """Run gradient descent with step size 1 / lambda_max(Q)."""
    eigvals = np.linalg.eigvalsh(q)
    if np.min(eigvals) <= 0:
        raise ValueError("Q must be positive definite for this experiment.")

    step_size = 1.0 / np.max(eigvals)
    x_star = -np.linalg.solve(q, b)
    f_star = quadratic_value(x_star, q, b)

    x = x0.astype(float).copy()
    gaps = []

    for _ in range(steps):
        gaps.append(max(quadratic_value(x, q, b) - f_star, 1e-18))
        grad = q @ x + b
        x = x - step_size * grad

    return np.arange(steps), np.asarray(gaps)


def main() -> None:
    b = np.array([0.4, -0.8])

    q_psd = np.array([[3.0, 0.5], [0.5, 1.0]])
    q_indefinite = np.array([[1.0, 0.0], [0.0, -0.5]])

    print("Sampled convexity inequality check")
    print("PSD quadratic violations:", convexity_violations(q_psd, b), "/ 5000")
    print(
        "Indefinite quadratic violations:",
        convexity_violations(q_indefinite, b),
        "/ 5000",
    )
    print("Note: zero sampled violations is not a mathematical proof.")

    x0 = np.array([4.0, -3.0])
    q_moderate = np.diag([1.0, 10.0])
    q_ill_conditioned = np.diag([1.0, 1000.0])

    k1, gap1 = gradient_descent_quadratic(q_moderate, b, x0)
    k2, gap2 = gradient_descent_quadratic(q_ill_conditioned, b, x0)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogy(k1, gap1, label="condition number = 10")
    ax.semilogy(k2, gap2, label="condition number = 1000")
    ax.set_xlabel("iteration")
    ax.set_ylabel("objective gap")
    ax.set_title("Gradient descent: conditioning changes convergence speed")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
