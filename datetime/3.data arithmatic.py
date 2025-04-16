import datetime

# Define a date
base_date = datetime.datetime(2023, 10, 5)

# Add 10 days
new_date = base_date + datetime.timedelta(days=10)

# Subtract 5 days
previous_date = base_date - datetime.timedelta(days=5)

# Display the results
print(f'Base date: {base_date}')
print(f'New date after adding 10 days: {new_date}')
print(f'Date after subtracting 5 days: {previous_date}')

