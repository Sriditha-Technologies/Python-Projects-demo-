import matplotlib.pyplot as plt

sizes=[5,6,7,8]
labels=["category A","category B","category C","category D"]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Pie chart")
plt.axis("equal")
plt.show()