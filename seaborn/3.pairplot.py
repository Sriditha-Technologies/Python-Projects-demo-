import seaborn as sns
import matplotlib.pyplot as plt

iris=sns.load_dataset('iris')
sns.pairplot(iris, hue='species', palette='Set1')
plt.title("seaborn pair plot")
plt.show()