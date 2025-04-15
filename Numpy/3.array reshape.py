import numpy as np

# Create a 1D array
one_d_array = np.arange(1, 13)

# Reshape into a 2D array (3 rows, 4 columns)
two_d_array = one_d_array.reshape(3, 4)

print("1D Array:", one_d_array)
print("Reshaped 2D Array:\n", two_d_array)