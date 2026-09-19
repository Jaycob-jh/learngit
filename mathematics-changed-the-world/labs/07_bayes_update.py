import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.stats import beta

rng = np.random.default_rng(7)
true_p = 0.72
observations = rng.binomial(1, true_p, size=120)
checkpoints = [0, 1, 2, 5, 10, 20, 50, 120]

grid = np.linspace(0.001, 0.999, 600)
alpha0, beta0 = 1.0, 1.0

fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.axvline(true_p, linestyle="--", label="true p")
ax.set_xlim(0.0, 1.0)
ax.set_ylim(0.0, 13.0)
ax.set_xlabel("coin bias p")
ax.set_ylabel("posterior density")
ax.legend()


def posterior_params(n):
    data = observations[:n]
    successes = int(data.sum())
    failures = n - successes
    return alpha0 + successes, beta0 + failures


def update(frame):
    n = checkpoints[frame]
    a, b = posterior_params(n)
    density = beta.pdf(grid, a, b)
    line.set_data(grid, density)
    ax.set_title(f"Beta-Bernoulli update after n={n} observations: Beta({a:.0f},{b:.0f})")
    return (line,)

ani = FuncAnimation(fig, update, frames=len(checkpoints), interval=900, repeat=True)
plt.tight_layout()
plt.show()
