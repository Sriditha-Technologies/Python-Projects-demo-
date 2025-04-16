import datetime

# Get today's date
today = datetime.date.today()

# Display today's date in different formats
print(f'Today\'s date: {today}')
print(f'Today\'s date (ISO format): {today.isoformat()}')
print(f'Today\'s date (formatted): {today.strftime("%d/%m/%Y")}')