import numpy as np
import matplotlib.pyplot as plt

# 2D analogue using F=(x, y), whose divergence is 2 everywhere.
# For square [-1,1]^2: integral(div F)dA = 2 * area = 8.
# Boundary outward flux is also 8.

n = 31
x = np.linspace(-1.0, 1.0, n)
y = np.linspace(-1.0, 1.0, n)
X, Y = np.meshgrid(x, y)
U, V = X, Y

dx = x[1] - x[0]
dy = y[1] - y[0]
divergence = np.gradient(U, dx, axis=1) + np.gradient(V, dy, axis=0)
interior_integral = np.trapezoid(
    np.trapezoid(divergence, x, axis=1),
    y,
    axis=0,
)

# On every side of the square, F dot n = 1, and each side has length 2.
boundary_flux = 8.0

print("discrete interior divergence integral ≈", interior_integral)
print("boundary flux =", boundary_flux)
print("exact value = 8")

plt.figure()
plt.quiver(X, Y, U, V)
plt.gca().set_aspect("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Vector field F=(x,y): a source field")
plt.tight_layout()
plt.show()
