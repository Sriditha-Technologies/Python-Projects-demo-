# Reading a file line by line
try:
    with open('dhamu.txt', 'r') as f:
        print("Reading lines from 'dhamu.txt':")
        for line in f:
            print(line.strip())  # .strip() removes leading/trailing whitespace
except FileNotFoundError:
    print("The file 'dhamu.txt' does not exist.")