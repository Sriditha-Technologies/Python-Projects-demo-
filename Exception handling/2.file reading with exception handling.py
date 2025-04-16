def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print("Error: An error occurred while reading the file.")

# Trying to read a non-existent file
read_file("non_existent_file.txt")