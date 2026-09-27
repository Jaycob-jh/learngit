"""Constrained optimization lab: penalty, ALM, and primal-dual interior points.

Supports PKU optimization study Unit 05.

Part A:
    equality-constrained quadratic
    -> quadratic penalty
    -> augmented Lagrangian multiplier updates

Part B:
    a two-variable linear program
    -> perturbed primal-dual KKT equations
    -> central-path tracking with Newton steps

The code is educational and intentionally small.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def equality_problem_data():
    q = np.array([2.0, -1.0])
    a = np.array([1.0, 1.0])
    b = 0.5

    multiplier_star = float((a @ q - b) / (a @ a))
    x_star = q - multiplier_star * a
    return q, a, b, x_star, multiplier_star


def quadratic_penalty_path(sigmas: np.ndarray):
    q, a, b, x_star, multiplier_star = equality_problem_data()

    xs = []
    violations = []
    condition_numbers = []
    multiplier_estimates = []

    for sigma in sigmas:
        hessian = np.eye(2) + sigma * np.outer(a, a)
        rhs = q + sigma * b * a
        x = np.linalg.solve(hessian, rhs)

        constraint_value = float(a @ x - b)
        xs.append(x)
        violations.append(abs(constraint_value))
        condition_numbers.append(np.linalg.cond(hessian))

        # The book's multiplier estimate for the equality quadratic penalty
        # has the sign -sigma*c(x).
        multiplier_estimates.append(-sigma * constraint_value)

    return {
        "x_star": x_star,
        "lambda_star": multiplier_star,
        "xs": np.asarray(xs),
        "violations": np.asarray(violations),
        "condition_numbers": np.asarray(condition_numbers),
        "multiplier_estimates": np.asarray(multiplier_estimates),
    }


def augmented_lagrangian_iterations(
    *,
    sigma: float = 5.0,
    iterations: int = 10,
):
    q, a, b, x_star, multiplier_star = equality_problem_data()

    multiplier = 0.0
    xs = []
    violations = []
    multipliers = []
    condition_numbers = []

    hessian = np.eye(2) + sigma * np.outer(a, a)

    for _ in range(iterations):
        rhs = q + (sigma * b - multiplier) * a
        x = np.linalg.solve(hessian, rhs)

        constraint_value = float(a @ x - b)

        xs.append(x)
        violations.append(abs(constraint_value))
        multipliers.append(multiplier)
        condition_numbers.append(np.linalg.cond(hessian))

        multiplier = multiplier + sigma * constraint_value

    multipliers.append(multiplier)

    return {
        "x_star": x_star,
        "lambda_star": multiplier_star,
        "xs": np.asarray(xs),
        "violations": np.asarray(violations),
        "multipliers": np.asarray(multipliers),
        "condition_numbers": np.asarray(condition_numbers),
    }


def penalty_vs_alm_demo() -> None:
    sigmas = 2.0 ** np.arange(-1, 10)

    penalty = quadratic_penalty_path(sigmas)
    alm = augmented_lagrangian_iterations(sigma=5.0, iterations=10)

    print("A. Equality-constrained quadratic")
    print("exact x* =", np.round(penalty["x_star"], 8))
    print("exact lambda* =", round(float(penalty["lambda_star"]), 8))

    print("\nQuadratic penalty:")
    for sigma, violation, cond, lam_est in zip(
        sigmas,
        penalty["violations"],
        penalty["condition_numbers"],
        penalty["multiplier_estimates"],
    ):
        print(
            f"  sigma={sigma:7.1f} "
            f"|constraint|={violation:.3e} "
            f"cond={cond:.3e} "
            f"-sigma*c={lam_est:.6f}"
        )

    print("\nAugmented Lagrangian with fixed sigma=5:")
    for k, (violation, cond) in enumerate(
        zip(alm["violations"], alm["condition_numbers"])
    ):
        print(
            f"  k={k:2d} "
            f"|constraint|={violation:.3e} "
            f"lambda_k={alm['multipliers'][k]:.8f} "
            f"cond={cond:.3e}"
        )
    print("  final lambda =", round(float(alm["multipliers"][-1]), 10))

    plt.figure(figsize=(8, 5))
    plt.loglog(
        sigmas,
        np.maximum(penalty["violations"], 1e-18),
        marker="o",
        label="quadratic penalty: constraint violation",
    )
    plt.loglog(
        sigmas,
        penalty["condition_numbers"],
        marker="o",
        label="quadratic penalty: Hessian condition number",
    )
    plt.xlabel("penalty sigma")
    plt.ylabel("magnitude")
    plt.title("Penalty method: feasibility improves while conditioning worsens")
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.semilogy(
        np.arange(len(alm["violations"])),
        np.maximum(alm["violations"], 1e-18),
        marker="o",
        label="ALM constraint violation",
    )
    plt.semilogy(
        np.arange(len(alm["condition_numbers"])),
        alm["condition_numbers"],
        marker="o",
        label="ALM inner Hessian condition number",
    )
    plt.xlabel("outer iteration")
    plt.ylabel("magnitude")
    plt.title("ALM: multiplier feedback with fixed finite penalty")
    plt.legend()
    plt.tight_layout()
    plt.show()


def primal_dual_central_path(
    taus: np.ndarray,
    *,
    tolerance: float = 1e-12,
    max_newton_steps: int = 80,
):
    """Track the central path for

    min x1 + 2 x2
    s.t. x1 + x2 = 1, x >= 0.

    Dual:
    max y
    s.t. [y, y] + s = [1, 2], s >= 0.
    """
    a = np.array([[1.0, 1.0]])
    b = np.array([1.0])
    c = np.array([1.0, 2.0])

    # Strictly positive warm start.
    x = np.array([0.5, 0.5])
    y = np.array([0.0])
    s = np.array([1.0, 2.0])

    records = []

    for tau in taus:
        for newton_step in range(max_newton_steps):
            primal_residual = a @ x - b
            dual_residual = a.T @ y + s - c
            complementarity_residual = x * s - tau * np.ones_like(x)

            residual_norm = max(
                np.linalg.norm(primal_residual),
                np.linalg.norm(dual_residual),
                np.linalg.norm(complementarity_residual),
            )
            if residual_norm <= tolerance:
                break

            system = np.block(
                [
                    [
                        a,
                        np.zeros((1, 1)),
                        np.zeros((1, 2)),
                    ],
                    [
                        np.zeros((2, 2)),
                        a.T,
                        np.eye(2),
                    ],
                    [
                        np.diag(s),
                        np.zeros((2, 1)),
                        np.diag(x),
                    ],
                ]
            )

            rhs = -np.concatenate(
                [
                    primal_residual,
                    dual_residual,
                    complementarity_residual,
                ]
            )

            direction = np.linalg.solve(system, rhs)
            dx = direction[:2]
            dy = direction[2:3]
            ds = direction[3:]

            # Keep x and s strictly positive.
            alpha = 1.0
            negative_dx = dx < 0.0
            negative_ds = ds < 0.0

            if np.any(negative_dx):
                alpha = min(
                    alpha,
                    0.99 * np.min(-x[negative_dx] / dx[negative_dx]),
                )
            if np.any(negative_ds):
                alpha = min(
                    alpha,
                    0.99 * np.min(-s[negative_ds] / ds[negative_ds]),
                )

            x = x + alpha * dx
            y = y + alpha * dy
            s = s + alpha * ds
        else:
            raise RuntimeError("Central-path Newton iteration did not converge.")

        primal_value = float(c @ x)
        dual_value = float(b @ y)
        gap = float(x @ s)

        records.append(
            {
                "tau": float(tau),
                "x": x.copy(),
                "y": y.copy(),
                "s": s.copy(),
                "primal_value": primal_value,
                "dual_value": dual_value,
                "gap": gap,
                "newton_steps": newton_step,
            }
        )

    return records


def interior_point_demo() -> None:
    taus = np.array([1.0, 0.3, 0.1, 0.03, 0.01, 0.003, 0.001])
    records = primal_dual_central_path(taus)

    print("\nB. Primal-dual central path")
    print("LP optimum is x*=(1,0), primal optimum=1, dual optimum=1.")
    for record in records:
        tau = record["tau"]
        x = record["x"]
        s = record["s"]
        print(
            f"  tau={tau:7.4f} "
            f"x={np.round(x, 6)} "
            f"s={np.round(s, 6)} "
            f"p={record['primal_value']:.6f} "
            f"d={record['dual_value']:.6f} "
            f"gap={record['gap']:.6f}"
        )

        # For n=2, the exact central-path identity is x^T s = 2*tau.
        assert np.isclose(record["gap"], 2.0 * tau, atol=1e-8)

    x2 = np.array([record["x"][1] for record in records])
    gaps = np.array([record["gap"] for record in records])
    primal_values = np.array(
        [record["primal_value"] for record in records]
    )
    dual_values = np.array(
        [record["dual_value"] for record in records]
    )

    plt.figure(figsize=(8, 5))
    plt.loglog(taus, x2, marker="o", label="x2 along central path")
    plt.loglog(taus, gaps, marker="o", label="primal-dual gap x^T s")
    plt.xlabel("central parameter tau")
    plt.ylabel("magnitude")
    plt.title("Interior-point path approaches the boundary and zero gap")
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.semilogx(taus, primal_values, marker="o", label="primal objective")
    plt.semilogx(taus, dual_values, marker="o", label="dual objective")
    plt.axhline(1.0, linestyle="--", label="optimal value")
    plt.xlabel("central parameter tau")
    plt.ylabel("objective value")
    plt.title("Primal and dual values meet as tau decreases")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main() -> None:
    penalty_vs_alm_demo()
    interior_point_demo()


if __name__ == "__main__":
    main()
