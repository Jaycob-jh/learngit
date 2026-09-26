"""Unconstrained optimization lab: one framework, several algorithms.

Supports PKU optimization study Unit 04.

Part A compares first-/second-order globalization strategies on Rosenbrock:
- gradient + Armijo
- Barzilai-Borwein + nonmonotone Armijo
- modified Newton + Armijo
- BFGS + Armijo
- trust-region quadratic model

Part B compares Gauss-Newton and a damped LM-style update on a nonlinear
least-squares curve-fitting problem.

The code is educational rather than production-grade.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt


@dataclass
class Result:
    name: str
    x: np.ndarray
    values: np.ndarray
    grad_norms: np.ndarray


def rosenbrock(x: np.ndarray) -> float:
    x1, x2 = x
    return float(100.0 * (x2 - x1**2) ** 2 + (1.0 - x1) ** 2)


def rosenbrock_grad(x: np.ndarray) -> np.ndarray:
    x1, x2 = x
    return np.array(
        [
            -400.0 * x1 * (x2 - x1**2) - 2.0 * (1.0 - x1),
            200.0 * (x2 - x1**2),
        ]
    )


def rosenbrock_hess(x: np.ndarray) -> np.ndarray:
    x1, x2 = x
    return np.array(
        [
            [1200.0 * x1**2 - 400.0 * x2 + 2.0, -400.0 * x1],
            [-400.0 * x1, 200.0],
        ]
    )


def armijo_backtracking(
    f,
    grad,
    x: np.ndarray,
    direction: np.ndarray,
    *,
    alpha0: float = 1.0,
    c1: float = 1e-4,
    beta: float = 0.5,
) -> float:
    """Return a step satisfying the Armijo sufficient-decrease test."""
    g = grad(x)
    directional_derivative = float(g @ direction)
    if directional_derivative >= 0.0:
        raise ValueError("Armijo requires a descent direction.")

    alpha = alpha0
    f0 = f(x)
    while (
        f(x + alpha * direction)
        > f0 + c1 * alpha * directional_derivative
    ):
        alpha *= beta
        if alpha < 1e-14:
            raise RuntimeError("Armijo backtracking produced a tiny step.")
    return alpha


def gradient_armijo(
    x0: np.ndarray,
    *,
    max_iter: int = 5000,
    tol: float = 1e-8,
) -> Result:
    x = x0.astype(float).copy()
    values = []
    grad_norms = []

    for _ in range(max_iter):
        g = rosenbrock_grad(x)
        values.append(rosenbrock(x))
        grad_norms.append(np.linalg.norm(g))
        if grad_norms[-1] <= tol:
            break

        direction = -g
        alpha = armijo_backtracking(
            rosenbrock,
            rosenbrock_grad,
            x,
            direction,
        )
        x = x + alpha * direction

    return Result(
        "Gradient + Armijo",
        x,
        np.asarray(values),
        np.asarray(grad_norms),
    )


def bb_nonmonotone(
    x0: np.ndarray,
    *,
    max_iter: int = 2500,
    tol: float = 1e-8,
    memory: int = 10,
) -> Result:
    """BB1 step from the book, safeguarded by nonmonotone Armijo."""
    x = x0.astype(float).copy()
    g = rosenbrock_grad(x)
    alpha = 1e-3

    values = [rosenbrock(x)]
    grad_norms = [np.linalg.norm(g)]

    for _ in range(max_iter):
        if grad_norms[-1] <= tol:
            break

        trial_alpha = float(np.clip(alpha, 1e-8, 1e2))
        reference = max(values[-(memory + 1) :])

        # Nonmonotone Armijo: compare against a short history window.
        while (
            rosenbrock(x - trial_alpha * g)
            > reference - 1e-4 * trial_alpha * float(g @ g)
        ):
            trial_alpha *= 0.5
            if trial_alpha < 1e-14:
                raise RuntimeError("BB line search produced a tiny step.")

        x_new = x - trial_alpha * g
        g_new = rosenbrock_grad(x_new)

        s = x_new - x
        y = g_new - g
        sy = float(s @ y)
        yy = float(y @ y)

        # Book notation:
        # alpha_BB1 = (s^T y)/(y^T y).
        if sy > 1e-14 and yy > 1e-14:
            alpha = sy / yy
        else:
            alpha = 1e-3

        x, g = x_new, g_new
        values.append(rosenbrock(x))
        grad_norms.append(np.linalg.norm(g))

    return Result(
        "BB + nonmonotone",
        x,
        np.asarray(values),
        np.asarray(grad_norms),
    )


def modified_newton_armijo(
    x0: np.ndarray,
    *,
    max_iter: int = 100,
    tol: float = 1e-8,
) -> Result:
    """Shift an indefinite Hessian, then use Armijo globalization."""
    x = x0.astype(float).copy()
    values = []
    grad_norms = []

    for _ in range(max_iter):
        g = rosenbrock_grad(x)
        values.append(rosenbrock(x))
        grad_norms.append(np.linalg.norm(g))
        if grad_norms[-1] <= tol:
            break

        h = rosenbrock_hess(x)
        min_eig = float(np.min(np.linalg.eigvalsh(h)))

        # E_k = tau_k I: make the model matrix safely positive definite.
        shift = max(0.0, 1e-6 - min_eig)
        model_hessian = h + shift * np.eye(x.size)

        direction = np.linalg.solve(model_hessian, -g)
        if float(g @ direction) >= 0.0:
            direction = -g

        alpha = armijo_backtracking(
            rosenbrock,
            rosenbrock_grad,
            x,
            direction,
        )
        x = x + alpha * direction

    return Result(
        "Modified Newton",
        x,
        np.asarray(values),
        np.asarray(grad_norms),
    )


def bfgs_armijo(
    x0: np.ndarray,
    *,
    max_iter: int = 500,
    tol: float = 1e-8,
) -> Result:
    """BFGS inverse-Hessian update with Armijo safeguarding."""
    x = x0.astype(float).copy()
    inverse_hessian = np.eye(x.size)
    g = rosenbrock_grad(x)

    values = [rosenbrock(x)]
    grad_norms = [np.linalg.norm(g)]

    for _ in range(max_iter):
        if grad_norms[-1] <= tol:
            break

        direction = -inverse_hessian @ g
        if float(g @ direction) >= 0.0:
            inverse_hessian = np.eye(x.size)
            direction = -g

        alpha = armijo_backtracking(
            rosenbrock,
            rosenbrock_grad,
            x,
            direction,
        )

        s = alpha * direction
        x_new = x + s
        g_new = rosenbrock_grad(x_new)
        y = g_new - g

        ys = float(y @ s)
        if ys > 1e-12:
            rho = 1.0 / ys
            identity = np.eye(x.size)
            v = identity - rho * np.outer(s, y)
            inverse_hessian = (
                v @ inverse_hessian @ v.T + rho * np.outer(s, s)
            )

        x, g = x_new, g_new
        values.append(rosenbrock(x))
        grad_norms.append(np.linalg.norm(g))

    return Result(
        "BFGS + Armijo",
        x,
        np.asarray(values),
        np.asarray(grad_norms),
    )


def solve_small_trust_region(
    g: np.ndarray,
    h: np.ndarray,
    radius: float,
) -> np.ndarray:
    """Solve a small symmetric quadratic trust-region subproblem.

    This eigenvalue/secular-equation implementation is for the 2-D teaching
    example. Large-scale trust-region methods would use Cauchy, dogleg,
    truncated-CG, or related approximate subproblem solvers.
    """
    eigenvalues, eigenvectors = np.linalg.eigh(h)
    transformed_g = eigenvectors.T @ g

    if np.min(eigenvalues) > 1e-12:
        newton_step = eigenvectors @ (-transformed_g / eigenvalues)
        if np.linalg.norm(newton_step) <= radius:
            return newton_step

    lower = max(1e-12, -float(np.min(eigenvalues)) + 1e-12)

    def step_for(lam: float) -> np.ndarray:
        return eigenvectors @ (-transformed_g / (eigenvalues + lam))

    lower_step = step_for(lower)

    # Approximate the rare hard case by completing the boundary step along the
    # minimum-eigenvalue direction.
    if np.linalg.norm(lower_step) < radius:
        direction = eigenvectors[:, int(np.argmin(eigenvalues))]
        b = 2.0 * float(lower_step @ direction)
        c = float(lower_step @ lower_step - radius**2)
        disc = max(0.0, b * b - 4.0 * c)
        roots = [(-b + np.sqrt(disc)) / 2.0, (-b - np.sqrt(disc)) / 2.0]
        candidates = [lower_step + t * direction for t in roots]
        model_values = [
            float(g @ d + 0.5 * d @ h @ d)
            for d in candidates
        ]
        return candidates[int(np.argmin(model_values))]

    upper = max(1.0, 2.0 * lower)
    while np.linalg.norm(step_for(upper)) > radius:
        upper *= 2.0

    for _ in range(80):
        middle = 0.5 * (lower + upper)
        if np.linalg.norm(step_for(middle)) > radius:
            lower = middle
        else:
            upper = middle

    return step_for(upper)


def trust_region_rosenbrock(
    x0: np.ndarray,
    *,
    max_iter: int = 500,
    tol: float = 1e-8,
    radius0: float = 1.0,
    radius_max: float = 100.0,
) -> Result:
    x = x0.astype(float).copy()
    radius = radius0

    values = []
    grad_norms = []

    for _ in range(max_iter):
        g = rosenbrock_grad(x)
        h = rosenbrock_hess(x)
        values.append(rosenbrock(x))
        grad_norms.append(np.linalg.norm(g))
        if grad_norms[-1] <= tol:
            break

        step = solve_small_trust_region(g, h, radius)

        predicted_reduction = -float(
            g @ step + 0.5 * step @ h @ step
        )
        actual_reduction = rosenbrock(x) - rosenbrock(x + step)

        if predicted_reduction <= 0.0:
            rho = -np.inf
        else:
            rho = actual_reduction / predicted_reduction

        step_norm = np.linalg.norm(step)

        if rho < 0.25:
            radius *= 0.25
        elif (
            rho > 0.75
            and abs(step_norm - radius) <= 1e-6 * max(1.0, radius)
        ):
            radius = min(2.0 * radius, radius_max)

        if rho > 0.1:
            x = x + step

    return Result(
        "Trust region",
        x,
        np.asarray(values),
        np.asarray(grad_norms),
    )


def nonlinear_residual(
    parameters: np.ndarray,
    t: np.ndarray,
    observed: np.ndarray,
) -> np.ndarray:
    a, b = parameters
    return a * np.exp(b * t) - observed


def nonlinear_jacobian(
    parameters: np.ndarray,
    t: np.ndarray,
) -> np.ndarray:
    a, b = parameters
    exponential = np.exp(b * t)
    return np.column_stack(
        [
            exponential,
            a * t * exponential,
        ]
    )


def gauss_newton(
    p0: np.ndarray,
    t: np.ndarray,
    observed: np.ndarray,
    *,
    max_iter: int = 80,
    tol: float = 1e-10,
) -> tuple[np.ndarray, np.ndarray]:
    p = p0.astype(float).copy()
    residual_norms = []

    for _ in range(max_iter):
        residual = nonlinear_residual(p, t, observed)
        jacobian = nonlinear_jacobian(p, t)
        gradient = jacobian.T @ residual

        residual_norms.append(np.linalg.norm(residual))
        if np.linalg.norm(gradient) <= tol:
            break

        # Solve min_d ||J d + r||_2 without explicitly forming (J^T J)^-1.
        direction, *_ = np.linalg.lstsq(jacobian, -residual, rcond=None)

        # Armijo on 0.5 ||r||^2.
        objective = 0.5 * float(residual @ residual)
        directional_derivative = float(gradient @ direction)
        alpha = 1.0

        while True:
            candidate = p + alpha * direction
            candidate_residual = nonlinear_residual(
                candidate,
                t,
                observed,
            )
            candidate_objective = 0.5 * float(
                candidate_residual @ candidate_residual
            )
            if (
                candidate_objective
                <= objective + 1e-4 * alpha * directional_derivative
            ):
                break
            alpha *= 0.5
            if alpha < 1e-14:
                raise RuntimeError("Gauss-Newton line search failed.")

        p = p + alpha * direction

    return p, np.asarray(residual_norms)


def levenberg_marquardt_demo(
    p0: np.ndarray,
    t: np.ndarray,
    observed: np.ndarray,
    *,
    max_iter: int = 100,
    tol: float = 1e-10,
    damping0: float = 1e-2,
) -> tuple[np.ndarray, np.ndarray]:
    """A simple damping illustration of the LM equation.

    The book presents LM as a trust-region method. This compact experiment
    adapts lambda using accept/reject logic to expose the role of
    (J^T J + lambda I) d = -J^T r.
    """
    p = p0.astype(float).copy()
    damping = damping0
    residual_norms = []

    for _ in range(max_iter):
        residual = nonlinear_residual(p, t, observed)
        jacobian = nonlinear_jacobian(p, t)
        gradient = jacobian.T @ residual

        residual_norms.append(np.linalg.norm(residual))
        if np.linalg.norm(gradient) <= tol:
            break

        normal_matrix = jacobian.T @ jacobian
        direction = np.linalg.solve(
            normal_matrix + damping * np.eye(p.size),
            -gradient,
        )

        current_objective = 0.5 * float(residual @ residual)
        candidate = p + direction
        candidate_residual = nonlinear_residual(
            candidate,
            t,
            observed,
        )
        candidate_objective = 0.5 * float(
            candidate_residual @ candidate_residual
        )

        if candidate_objective < current_objective:
            p = candidate
            damping = max(damping / 3.0, 1e-12)
        else:
            damping = min(damping * 10.0, 1e12)

    return p, np.asarray(residual_norms)


def compare_rosenbrock_methods() -> None:
    x0 = np.array([-1.2, 1.0])

    results = [
        gradient_armijo(x0),
        bb_nonmonotone(x0),
        modified_newton_armijo(x0),
        bfgs_armijo(x0),
        trust_region_rosenbrock(x0),
    ]

    print("A. Rosenbrock comparison")
    for result in results:
        iterations = len(result.grad_norms) - 1
        print(
            f"{result.name:24s} "
            f"iterations={iterations:4d} "
            f"f={result.values[-1]:.3e} "
            f"||g||={result.grad_norms[-1]:.3e} "
            f"x={np.round(result.x, 6)}"
        )

    plt.figure(figsize=(9, 5))
    for result in results:
        plt.semilogy(
            np.arange(len(result.grad_norms)),
            np.maximum(result.grad_norms, 1e-18),
            label=result.name,
        )
    plt.xlabel("iteration")
    plt.ylabel("gradient norm")
    plt.title("Rosenbrock: globalization and curvature information")
    plt.legend()
    plt.tight_layout()
    plt.show()


def compare_nonlinear_least_squares() -> None:
    rng = np.random.default_rng(21)
    t = np.linspace(0.0, 2.0, 60)
    true_parameters = np.array([2.5, -1.3])
    observed = (
        true_parameters[0] * np.exp(true_parameters[1] * t)
        + 0.02 * rng.normal(size=t.size)
    )

    p0 = np.array([1.0, 1.0])

    gauss_parameters, gauss_history = gauss_newton(
        p0,
        t,
        observed,
    )
    lm_parameters, lm_history = levenberg_marquardt_demo(
        p0,
        t,
        observed,
    )

    print("\nB. Nonlinear least squares")
    print("true parameters:", true_parameters)
    print(
        "Gauss-Newton:",
        np.round(gauss_parameters, 6),
        "iterations=",
        len(gauss_history) - 1,
    )
    print(
        "LM-style:",
        np.round(lm_parameters, 6),
        "iterations=",
        len(lm_history) - 1,
    )

    plt.figure(figsize=(8, 5))
    plt.semilogy(
        np.arange(len(gauss_history)),
        gauss_history,
        label="Gauss-Newton residual norm",
    )
    plt.semilogy(
        np.arange(len(lm_history)),
        lm_history,
        label="LM-style residual norm",
    )
    plt.xlabel("iteration")
    plt.ylabel("residual norm")
    plt.title("Nonlinear least squares: structure-aware methods")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main() -> None:
    compare_rosenbrock_methods()
    compare_nonlinear_least_squares()


if __name__ == "__main__":
    main()
