import pandas as pd

# Create a DataFrame
data = {
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'IT'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Edward', 'Frank'],
    'Salary': [50000, 60000, 70000, 80000, 90000, 95000]
}

df = pd.DataFrame(data)

# Group by department and calculate the average salary
grouped_df = df.groupby('Department')['Salary'].mean().reset_index()

# Display the grouped DataFrame
print(grouped_df)