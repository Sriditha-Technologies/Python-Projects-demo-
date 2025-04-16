def convert_to_float(value):
    try:
        number = float(value)
        print(f"The float value is: {number}")
    except ValueError:
        print(f"Error: '{value}' is not a valid number.")

# Using the function
convert_to_float("3.14")    # valid number
convert_to_float("hello")    # invalid number
convert_to_float("123abc")   # invalid number