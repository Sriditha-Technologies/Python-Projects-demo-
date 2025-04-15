import numpy as np

data=np.array([2,4,6,8,10,11])

#calculate statistics
minimum=np.min(data)
maximum=np.max(data)
mean=np.mean(data)
median=np.median(data)
variance=np.var(data)
std_dev=np.std(data)

print("Minimum:",minimum)
print("Maximum:",maximum)
print("Mean:",mean)
print("Median:",median)
print("Variance:",variance)
print("Standared Deviation:",std_dev)
