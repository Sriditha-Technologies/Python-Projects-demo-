# Counting words in a file
try:
    with open('dhamu.txt', 'r') as f:
        content = f.read()
        word_count = len(content.split())
        print(f"The file 'dhamu.txt' contains {word_count} words.")
except FileNotFoundError:
    print("The file 'example.txt' does not exist.")