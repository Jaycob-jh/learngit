import numpy as np
import matplotlib.pyplot as plt

sample_rate = 1000.0
duration = 2.0
t = np.arange(0.0, duration, 1.0 / sample_rate)

signal = (
    1.0 * np.sin(2.0 * np.pi * 5.0 * t)
    + 0.6 * np.sin(2.0 * np.pi * 17.0 * t + 0.4)
    + 0.25 * np.sin(2.0 * np.pi * 40.0 * t)
)

spectrum = np.fft.rfft(signal)
freq = np.fft.rfftfreq(len(signal), d=1.0 / sample_rate)
amplitude = 2.0 * np.abs(spectrum) / len(signal)

peak_idx = np.argsort(amplitude)[-6:][::-1]
print("largest frequency bins (Hz):", freq[peak_idx])

plt.figure()
plt.plot(t[:500], signal[:500])
plt.xlabel("time (s)")
plt.ylabel("amplitude")
plt.title("Time domain")
plt.tight_layout()

plt.figure()
plt.plot(freq, amplitude)
plt.xlim(0, 80)
plt.xlabel("frequency (Hz)")
plt.ylabel("amplitude")
plt.title("Frequency domain via FFT")
plt.tight_layout()
plt.show()
