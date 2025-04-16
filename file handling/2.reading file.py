# Reading from a file
try:
    with open('dhamu.txt', 'r') as f:
        content = f.read()
        print("Content of 'dhamu.txt':")
        print(content)
except FileNotFoundError:
    print("The file 'example.txt' does not exist.")