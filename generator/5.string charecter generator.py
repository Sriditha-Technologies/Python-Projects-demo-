def character_generator(s):
    for char in s:
        yield char

# Using the generator
text = "Hello, dhamu!"
char_gen = character_generator(text)

# Print each character from the string
for char in char_gen:
    print(char)