import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

# Create a new column 'Tax' based on 'Salary' using a lambda function
df['Tax'] = df['Salary'].apply(lambda x: x * 0.3)

# Display the DataFrame
print(df)