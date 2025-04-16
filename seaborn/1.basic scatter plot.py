import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
sns.scatterplot(data=tips , y='tip', x='total_bill', hue='day')
plt.title("seaborn scatter plot")
plt.show()