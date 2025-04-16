import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
sns.boxplot(data=tips, x='tip', y='total_bill', palette='Set2')
plt.title("seaborn box plot")
plt.show()