import matplotlib.pyplot as plt

x=[7,9,3,2,1]
y=[123,213,342,432,564]

plt.scatter(x,y , color="purple",marker='x')

plt.title("scatter plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()