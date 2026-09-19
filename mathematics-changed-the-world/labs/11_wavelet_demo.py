import numpy as np
import matplotlib.pyplot as plt


def haar_decompose(signal, levels=5):
    approx = np.asarray(signal, dtype=float).copy()
    details = []
    for _ in range(levels):
        if len(approx) % 2:
            raise ValueError("Haar demo requires an even signal length at every level")
        even = approx[0::2]
        odd = approx[1::2]
        next_approx = (even + odd) / np.sqrt(2.0)
        detail = (even - odd) / np.sqrt(2.0)
        details.append(detail)
        approx = next_approx
    return approx, details


def haar_reconstruct(approx, details):
    current = np.asarray(approx, dtype=float).copy()
    for detail in reversed(details):
        out = np.empty(current.size * 2, dtype=float)
        out[0::2] = (current + detail) / np.sqrt(2.0)
        out[1::2] = (current - detail) / np.sqrt(2.0)
        current = out
    return current


n = 1024
t = np.linspace(0.0, 1.0, n, endpoint=False)
signal = np.sin(2.0 * np.pi * 6.0 * t)
mask = (t > 0.45) & (t < 0.58)
signal += mask * 0.8 * np.sin(2.0 * np.pi * 90.0 * t)

approx, details = haar_decompose(signal, levels=5)
reconstructed = haar_reconstruct(approx, details)
print("Haar detail lengths:", [len(d) for d in details])
print("reconstruction RMSE:", np.sqrt(np.mean((signal - reconstructed) ** 2)))

plt.figure()
plt.plot(t, signal)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("Signal with a localized high-frequency burst")
plt.tight_layout()

for level, detail in enumerate(details, start=1):
    plt.figure()
    plt.plot(detail)
    plt.xlabel("coefficient index")
    plt.ylabel("detail coefficient")
    plt.title(f"Haar detail coefficients: level {level}")
    plt.tight_layout()

plt.show()
