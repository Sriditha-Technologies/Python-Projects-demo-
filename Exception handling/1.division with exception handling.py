def safe_divide(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Please provide numbers only.")

# Using the function
safe_divide(10, 2)  # valid division
safe_divide(10, 0)  # division by zero
safe_divide(10, "a")  # invalid input