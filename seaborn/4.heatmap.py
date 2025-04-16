import seaborn as sns
import matplotlib.pyplot as plt

# Load the flight dataset
flights = sns.load_dataset('flights').pivot('month', 'year', 'passengers')

# Create a heatmap
sns.heatmap(flights, cmap='YlGnBu', annot=True, fmt="d")
plt.title('Heatmap of Passengers over Time')
plt.show()