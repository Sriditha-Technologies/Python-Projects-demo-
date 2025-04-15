import matplotlib.pyplot  as plt
x=([1,2,3,4,5,6])
y=([2,4,6,8,10,11])

plt.plot(x, y, marker='o')
plt.title("Basic Line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.grid()
plt.show()