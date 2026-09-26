"""Optimality lab: stationary points, KKT regularity, and Slater duality.

Supports PKU optimization study Unit 03.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def stationary_point_demo() -> None:
    """Compare x^3 and x^4 at x=0."""
    x0 = 0.0

    grad_cubic = 3.0 * x0**2
    hess_cubic = 6.0 * x0
    grad_quartic = 4.0 * x0**3
    hess_quartic = 12.0 * x0**2

    print("A. Stationary points")
    print(f"x^3 at 0: gradient={grad_cubic:.1f}, Hessian={hess_cubic:.1f}")
    print("  0 is not a local minimum.")
    print(f"x^4 at 0: gradient={grad_quartic:.1f}, Hessian={hess_quartic:.1f}")
    print("  0 is a global minimum although the Hessian is zero.")

    grid = np.linspace(-1.25, 1.25, 500)
    plt.figure(figsize=(8, 5))
    plt.plot(grid, grid**3, label="x^3")
    plt.plot(grid, grid**4, label="x^4")
    plt.axhline(0.0, linewidth=0.8)
    plt.axvline(0.0, linewidth=0.8)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Stationarity and second-order conditions")
    plt.legend()
    plt.tight_layout()
    plt.show()


def kkt_constraint_qualification_demo() -> None:
    """Compare regular and degenerate descriptions of the same feasible set."""
    x_star = 0.0
    objective_gradient = 1.0  # f(x) = x

    # Regular equality c(x)=x=0.
    regular_constraint_gradient = 1.0
    regular_multiplier = -objective_gradient / regular_constraint_gradient
    regular_stationarity = (
        objective_gradient + regular_multiplier * regular_constraint_gradient
    )

    # Degenerate equality c(x)=x^2=0.
    degenerate_constraint_gradient = 2.0 * x_star

    print("\nB. KKT and constraint qualification")
    print("Problem: minimize x over the feasible set {0}.")
    print("Representation c(x)=x=0:")
    print("  constraint gradient at 0 =", regular_constraint_gradient)
    print("  KKT multiplier =", regular_multiplier)
    print("  stationarity residual =", regular_stationarity)

    print("Representation c(x)=x^2=0:")
    print("  constraint gradient at 0 =", degenerate_constraint_gradient)
    print("  stationarity becomes 1 + nu*0 = 0, so no multiplier solves it.")
    print("  The feasible set and global optimum are unchanged.")
    print("  KKT fails because the needed constraint qualification degenerates.")

    assert np.isclose(regular_stationarity, 0.0)
    assert np.isclose(degenerate_constraint_gradient, 0.0)


def slater_strong_duality_demo() -> None:
    """Check KKT and strong duality for min (x-2)^2 subject to x <= 1."""
    x_star = 1.0
    lambda_star = 2.0

    primal_value = (x_star - 2.0) ** 2
    constraint_value = x_star - 1.0

    stationarity = 2.0 * (x_star - 2.0) + lambda_star
    primal_feasible = constraint_value <= 1e-12
    dual_feasible = lambda_star >= 0.0
    complementary_slackness = lambda_star * constraint_value

    def dual_function(lam: np.ndarray) -> np.ndarray:
        return lam - 0.25 * lam**2

    dual_value = float(dual_function(np.array(lambda_star)))
    duality_gap = primal_value - dual_value

    slater_point = 0.0
    slater_strict = slater_point - 1.0 < 0.0

    print("\nC. Convex problem with Slater")
    print("Problem: minimize (x-2)^2 subject to x <= 1.")
    print("Slater test point x=0 gives c(x)=-1 < 0:", slater_strict)
    print("x* =", x_star, "lambda* =", lambda_star)
    print("stationarity residual =", stationarity)
    print("primal feasible =", primal_feasible)
    print("dual feasible =", dual_feasible)
    print("complementary-slackness residual =", complementary_slackness)
    print("primal optimum p* =", primal_value)
    print("dual optimum d* =", dual_value)
    print("duality gap p*-d* =", duality_gap)

    assert slater_strict
    assert np.isclose(stationarity, 0.0)
    assert primal_feasible
    assert dual_feasible
    assert np.isclose(complementary_slackness, 0.0)
    assert np.isclose(duality_gap, 0.0)

    lam = np.linspace(0.0, 4.0, 400)
    g = dual_function(lam)

    plt.figure(figsize=(8, 5))
    plt.plot(lam, g, label="dual function g(lambda)")
    plt.axhline(primal_value, linestyle="--", label="primal optimum p*=1")
    plt.scatter([lambda_star], [dual_value], label="dual optimum lambda*=2")
    plt.xlabel("lambda")
    plt.ylabel("dual value")
    plt.title("Strong duality in a Slater-regular convex problem")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main() -> None:
    stationary_point_demo()
    kkt_constraint_qualification_demo()
    slater_strong_duality_demo()


if __name__ == "__main__":
    main()
