import matplotlib.pyplot as plt

categories=['A','B','C','D']
values=[7,4,3,2]

plt.bar(categories,values,color="blue")

plt.title("Bar Chart")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()