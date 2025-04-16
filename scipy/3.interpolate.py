import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Given data points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 0, 1, 0, 1])

# Create an interpolation function
f = interp1d(x, y, kind='linear')

# Generate new x values for interpolation
x_new = np.linspace(0, 5, num=50)
y_new = f(x_new)

# Plot original points and interpolation
plt.plot(x, y, 'o', label='Original Data')
plt.plot(x_new, y_new, '-', label='Linear Interpolation')
plt.title('Linear Interpolation Example')
plt.legend()
plt.grid()
plt.show()
