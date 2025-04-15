import matplotlib.pyplot as plt
import numpy as np

data=np.random.randn(1000)

plt.hist(data,bins=30,color="lightgreen",edgecolor="black")

plt.title("Histogram of random data")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()