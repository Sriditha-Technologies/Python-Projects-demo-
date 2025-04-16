def add(x, y):
    return x + y
print("Addition: ", add(10, 5))        # Output: Addition:  15
def subtract(x, y):
    return x - y
print("Subtraction: ", subtract(10, 5))  # Output: Subtraction:  5
def multiply(x, y):
    return x * y
print("Multiplication: ", multiply(10, 5))  # Output: Multiplication:  50
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y
print("Division: ", divide(10, 5))        # Output: Division:  2.0
print("Division by zero: ", divide(10, 0)) # Output: Cannot divide by zero!