import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}

df = pd.DataFrame(data)

# Filter for employees aged 30 or older
filtered_df = df[df['Age'] >= 30]

# Display the filtered DataFrame
print(filtered_df)