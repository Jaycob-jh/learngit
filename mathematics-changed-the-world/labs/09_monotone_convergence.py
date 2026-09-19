import numpy as np
import matplotlib.pyplot as plt

# Target function f(x)=x on [0,1].
# f_n is the left-endpoint step approximation on dyadic intervals.

x = np.linspace(0.0, 1.0, 2001)
levels = [1, 2, 3, 4, 5, 6]

plt.figure()
plt.plot(x, x, linewidth=2, label="f(x)=x")

for n in levels:
    m = 2 ** n
    f_n = np.floor(m * x) / m
    f_n[-1] = 1.0
    numerical_integral = np.trapz(f_n, x)
    exact_step_integral = (m - 1) / (2.0 * m) + 1.0 / (2.0 * m * m)
    print(
        f"n={n:2d}, numerical integral={numerical_integral:.8f}, "
        f"step integral≈{exact_step_integral:.8f}"
    )
    plt.step(x, f_n, where="post", alpha=0.45, label=f"f_{n}")

print("target integral = 0.5")
plt.xlabel("x")
plt.ylabel("value")
plt.title("Monotone step functions approaching f(x)=x")
plt.legend(ncol=2)
plt.tight_layout()
plt.show()
