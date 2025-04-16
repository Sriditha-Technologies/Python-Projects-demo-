import numpy as np
from scipy.optimize import minimize

# Define a simple quadratic function
def func(x):
    return (x - 3)**2 + 4

# Use scipy's minimize function to find the minimum
result = minimize(func, x0=0)  # Starting point guess x0=0

print(f'Minimum value found at x = {result.x[0]}, f(x) = {result.fun}')