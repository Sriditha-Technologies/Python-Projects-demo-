# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter with a lambda function to find even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Display the even numbers
print(f'The even numbers are: {even_numbers}')