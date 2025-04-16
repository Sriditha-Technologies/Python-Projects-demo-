import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Create a sample signal
sampling_rate = 1000  # Sampling rate in Hz
T = 1.0 / sampling_rate  # Sample spacing
x = np.linspace(0.0, 1.0, sampling_rate)
freq = 5  # Frequency in Hz
y = 0.5 * np.sin(2 * np.pi * freq * x) + 0.5 * np.sin(2 * np.pi * 50 * x)  # Mixed frequency signal

# Compute the Fourier Transform
yf = fft(y)
xf = fftfreq(sampling_rate, T)[:sampling_rate // 2]

# Plot the signal and its Fourier Transform
plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title('Signal')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(xf, 2.0 / sampling_rate * np.abs(yf[:sampling_rate // 2]))
plt.title('Fourier Transform')
plt.grid()

plt.tight_layout()
plt.show()