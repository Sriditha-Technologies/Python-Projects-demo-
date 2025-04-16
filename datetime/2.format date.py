import datetime

# Define a specific date
specific_date = datetime.datetime(2023, 10, 5)

# Format the date in a more readable form
formatted_date = specific_date.strftime("%B %d, %Y")

# Display the formatted date
print(f'Formatted date: {formatted_date}')