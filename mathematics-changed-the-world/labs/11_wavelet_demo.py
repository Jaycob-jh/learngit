import numpy as np
import matplotlib.pyplot as plt
import pywt

n = 1024
t = np.linspace(0.0, 1.0, n, endpoint=False)

# A signal with a slow oscillation plus a short high-frequency burst.
signal = np.sin(2.0 * np.pi * 6.0 * t)
burst = (t > 0.45) & (t < 0.58)
signal = signal + burst * 0.8 * np.sin(2.0 * np.pi * 90.0 * t)

coeffs = pywt.wavedec(signal, "db4", level=5)
reconstructed = pywt.waverec(coeffs, "db4")[:n]

print("coefficient lengths:", [len(c) for c in coeffs])
print("reconstruction RMSE:", np.sqrt(np.mean((signal - reconstructed) ** 2)))

plt.figure()
plt.plot(t, signal)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("Signal with a localized high-frequency burst")
plt.tight_layout()

for level, detail in enumerate(coeffs[1:], start=1):
    plt.figure()
    plt.plot(detail)
    plt.xlabel("coefficient index")
    plt.ylabel("detail coefficient")
    plt.title(f"Wavelet detail coefficients: level {level}")
    plt.tight_layout()

plt.show()
