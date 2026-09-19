import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(-2.0 * np.pi, 2.0 * np.pi, 800)
true_y = np.sin(x)
orders = [1, 3, 5, 7, 9, 11, 13]


def sin_taylor(x_values, order):
    y = np.zeros_like(x_values)
    for k in range((order + 1) // 2):
        power = 2 * k + 1
        y += ((-1) ** k) * x_values ** power / math.factorial(power)
    return y

fig, ax = plt.subplots()
ax.plot(x, true_y, label="sin(x)")
approx_line, = ax.plot([], [], label="Taylor approximation")
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-2.0, 2.0)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()


def update(frame):
    order = orders[frame]
    approx_line.set_data(x, sin_taylor(x, order))
    ax.set_title(f"Taylor polynomial around 0, order {order}")
    return (approx_line,)

ani = FuncAnimation(fig, update, frames=len(orders), interval=900, repeat=True)
plt.tight_layout()
plt.show()
