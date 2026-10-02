"""Explore the Fourier-Laplace-Z transform family on a first-order stable system.

The script is a teaching experiment, not a general-purpose discretization library.
It compares:
1. a continuous pole in the s-plane;
2. the exact sampled mode z = exp(sT);
3. the frequency response of the analog first-order system and its exact
   zero-order-hold sampled-state recurrence;
4. the bilinear (Tustin) frequency warping relation.
"""

from __future__ import annotations

import argparse

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tau", type=float, default=0.5, help="time constant, seconds")
    parser.add_argument("--dt", type=float, default=0.05, help="sampling period, seconds")
    parser.add_argument("--points", type=int, default=800, help="frequency-grid size")
    args = parser.parse_args()

    if args.tau <= 0.0:
        parser.error("--tau must be positive")
    if args.dt <= 0.0:
        parser.error("--dt must be positive")
    if args.points < 50:
        parser.error("--points must be at least 50")

    tau = args.tau
    dt = args.dt
    analog_pole = -1.0 / tau
    discrete_pole = np.exp(analog_pole * dt)

    print(f"continuous pole s = {analog_pole:.6g}")
    print(f"sampled pole z = exp(sT) = {discrete_pole:.6g}")
    print("continuous stable?", analog_pole < 0.0)
    print("discrete stable?", abs(discrete_pole) < 1.0)

    omega0 = 3.0
    omega_alias = omega0 + 2.0 * np.pi / dt
    z0 = np.exp(1j * omega0 * dt)
    z_alias = np.exp(1j * omega_alias * dt)
    print(
        "aliasing map difference |z(omega)-z(omega+2pi/T)| =",
        abs(z0 - z_alias),
    )

    imag = np.linspace(-8.0 / tau, 8.0 / tau, args.points)
    plt.figure()
    plt.plot(np.zeros_like(imag), imag, linestyle="--", label="imaginary axis")
    plt.scatter([analog_pole], [0.0], s=70, marker="x", label="analog pole")
    plt.axvline(0.0, linewidth=0.8)
    plt.axhline(0.0, linewidth=0.8)
    plt.xlabel("Re(s)")
    plt.ylabel("Im(s)")
    plt.title("s-plane: stable first-order pole")
    plt.legend()
    plt.tight_layout()

    theta = np.linspace(0.0, 2.0 * np.pi, args.points)
    plt.figure()
    plt.plot(np.cos(theta), np.sin(theta), linestyle="--", label="unit circle")
    plt.scatter([discrete_pole], [0.0], s=70, marker="x", label="sampled pole")
    plt.axvline(0.0, linewidth=0.8)
    plt.axhline(0.0, linewidth=0.8)
    plt.axis("equal")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.title("z-plane: z = exp(sT)")
    plt.legend()
    plt.tight_layout()

    omega = np.linspace(0.0, 0.95 * np.pi / dt, args.points)
    h_analog = 1.0 / (1.0 + 1j * omega * tau)

    Omega = omega * dt
    alpha = discrete_pole
    z_inv = np.exp(-1j * Omega)
    h_discrete = (1.0 - alpha) * z_inv / (1.0 - alpha * z_inv)

    plt.figure()
    plt.plot(omega, 20.0 * np.log10(np.abs(h_analog)), label="analog |H(jw)|")
    plt.plot(
        omega,
        20.0 * np.log10(np.abs(h_discrete)),
        label="sampled ZOH recurrence |H(e^jW)|",
    )
    plt.xlabel("analog frequency w (rad/s)")
    plt.ylabel("magnitude (dB)")
    plt.title("Continuous and sampled first-order frequency response")
    plt.legend()
    plt.tight_layout()

    Omega_warp = np.linspace(0.0, 0.98 * np.pi, args.points)
    omega_warp = (2.0 / dt) * np.tan(Omega_warp / 2.0)

    plt.figure()
    plt.plot(Omega_warp, omega_warp)
    plt.xlabel("digital frequency Omega (rad/sample)")
    plt.ylabel("analog frequency w (rad/s)")
    plt.title("Bilinear transform frequency warping")
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()
