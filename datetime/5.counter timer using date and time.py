import datetime
import time

# Define the target date (New Year's Day)
target_date = datetime.datetime(2024, 1, 1)

# Infinite loop until the target date
while True:
    now = datetime.datetime.now()
    # Calculate the difference between the current time and the target date
    time_remaining = target_date - now
    
    if time_remaining.total_seconds() > 0:
        print(f'Time remaining until {target_date}: {time_remaining}')
        time.sleep(1)  # Wait for 1 second before rechecking
    else:
        print(f'Happy New Year! {target_date} has arrived!')
        break