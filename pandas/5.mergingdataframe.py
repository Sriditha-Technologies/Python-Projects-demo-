import pandas as pd

# Create two DataFrames
data1 = {
    'Employee': ['Alice', 'Bob', 'Charlie'],
    'Department': ['HR', 'IT', 'Finance'],
}

data2 = {
    'Employee': ['Bob', 'Alice', 'David'],
    'Salary': [60000, 50000, 70000],
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge the DataFrames on the 'Employee' column
merged_df = pd.merge(df1, df2, on='Employee')

# Display the merged DataFrame
print(merged_df)