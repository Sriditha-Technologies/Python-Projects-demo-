def simple_generator():
    for i in range(1, 6):
        yield i

# Using the generator
gen = simple_generator()

for number in gen:
   print(number)