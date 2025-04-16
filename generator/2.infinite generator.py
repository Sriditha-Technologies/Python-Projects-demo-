def infinite_generator():
    n = 1
    while True:
        yield n
        n += 1

# Using the generator
gen = infinite_generator()

# Print the first 10 numbers from the infinite generator
for _ in range(10):
    print(next(gen))