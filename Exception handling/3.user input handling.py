def get_integer_input():
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            print(f"You entered: {user_input}")
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Error: That's not a valid integer. Please try again.")

# Using the function
get_integer_input()