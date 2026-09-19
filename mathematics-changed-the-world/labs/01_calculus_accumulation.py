import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

x = np.linspace(0.0, 2.0 * np.pi, 1000)
f = np.sin(x)
A = cumulative_trapezoid(f, x, initial=0.0)
dA = np.gradient(A, x)

print("max |A'(x)-f(x)| =", np.max(np.abs(dA[2:-2] - f[2:-2])))

plt.figure()
plt.plot(x, f, label="f(x)=sin(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Local quantity: f(x)")
plt.legend()
plt.tight_layout()

plt.figure()
plt.plot(x, A, label="A(x)=integral_0^x f(t)dt")
plt.xlabel("x")
plt.ylabel("A(x)")
plt.title("Accumulation function")
plt.legend()
plt.tight_layout()

plt.figure()
plt.plot(x, dA, label="numerical derivative of A")
plt.plot(x, f, linestyle="--", label="f(x)")
plt.xlabel("x")
plt.ylabel("value")
plt.title("Fundamental theorem: A'(x) ≈ f(x)")
plt.legend()
plt.tight_layout()
plt.show()
