# List of tuples
data = [('apple', 4), ('banana', 2), ('orange', 3)]

# Sort the list by the second element of each tuple
sorted_data = sorted(data, key=lambda x: x[1])

# Display the sorted list
print(f'Sorted data: {sorted_data}')