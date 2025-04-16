def access_list_element(a_list, index):
    try:
        print(f"Element at index {index}: {a_list[index]}")
    except IndexError:
        print(f"Error: Index {index} is out of range for the given list.")
    except TypeError:
        print("Error: Please provide a valid index.")

# Using the function
my_list = [10, 20, 30]

access_list_element(my_list, 1)    # valid index
access_list_element(my_list, 5)    # invalid index
access_list_element(my_list, "a")   # invalid index type