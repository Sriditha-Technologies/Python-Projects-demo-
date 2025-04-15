def sum_of_digits(number):
    total=0
    while number > 0:
        digit = number % 10  # Get the last digit
        total += digit       # Add it to the total
        number //= 10        # Remove the last digit
    return total

number = int(input("Enter a number to find the sum of its digits: "))
print(f"The sum of the digits is: {sum_of_digits(number)}")