import numpy as np

# Generate an array of 10 random numbers between 0 and 100
random_numbers = np.random.randint(0, 101, size=10)

# Calculate mean and standard deviation
mean = np.mean(random_numbers)
std_dev = np.std(random_numbers)

print("Random Numbers:", random_numbers)
print("Mean:", mean)
print("Standard Deviation:", std_dev)