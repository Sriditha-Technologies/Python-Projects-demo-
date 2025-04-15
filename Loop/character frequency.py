def character_frequency(string):
    frequency = {}
    
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1  # Update count
    
    return frequency

text = input("Enter a string: ")
freq = character_frequency(text)
print("Character frequency:")
for char, count in freq.items():
    print(f"{char}: {count}")