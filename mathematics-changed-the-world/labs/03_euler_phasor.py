import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

theta = np.linspace(0.0, 2.0 * np.pi, 240)
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)
ax.set_xlabel("Re")
ax.set_ylabel("Im")

circle_t = np.linspace(0.0, 2.0 * np.pi, 400)
ax.plot(np.cos(circle_t), np.sin(circle_t), linewidth=1)
phasor, = ax.plot([], [], marker="o")
projection, = ax.plot([], [], linestyle="--")


def update(frame):
    t = theta[frame]
    z = np.exp(1j * t)
    phasor.set_data([0.0, z.real], [0.0, z.imag])
    projection.set_data([z.real, z.real], [0.0, z.imag])
    ax.set_title(f"e^(iθ) = cos θ + i sin θ, θ={t:.2f}")
    return phasor, projection

ani = FuncAnimation(fig, update, frames=len(theta), interval=35, repeat=True)
plt.tight_layout()
plt.show()
