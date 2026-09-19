import numpy as np
import matplotlib.pyplot as plt


def contour_integral(center=0.0 + 0.0j, radius=1.0, singularity=0.2 + 0.1j, n=200000):
    theta = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    z = center + radius * np.exp(1j * theta)
    dz = 1j * radius * np.exp(1j * theta) * (2.0 * np.pi / n)
    f = 1.0 / (z - singularity)
    return np.sum(f * dz), z

inside_value, path = contour_integral(singularity=0.2 + 0.1j)
outside_value, _ = contour_integral(singularity=2.0 + 0.0j)

print("singularity inside contour:", inside_value)
print("expected:", 2j * np.pi)
print("singularity outside contour:", outside_value)
print("expected: approximately 0")

plt.figure()
plt.plot(path.real, path.imag)
plt.scatter([0.2], [0.1], label="pole inside")
plt.scatter([2.0], [0.0], label="pole outside")
plt.gca().set_aspect("equal")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.title("Contour and poles")
plt.legend()
plt.tight_layout()
plt.show()
