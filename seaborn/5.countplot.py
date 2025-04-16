import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips')

# Create a count plot
sns.countplot(data=tips, x='day', palette='pastel')
plt.title('Count of Tips per Day')
plt.show()
