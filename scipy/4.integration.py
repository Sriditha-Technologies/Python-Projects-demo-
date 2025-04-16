import numpy as np
from scipy.integrate import quad

# Define a function to integrate
def integrand(x):
    return np.sin(x)

# Perform definite integration from 0 to pi
result, error = quad(integrand, 0, np.pi)

print(f'Integral of sin(x) from 0 to pi is: {result}, with an error estimate of: {error}')