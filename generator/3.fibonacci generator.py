def fibonacci_generator(max_terms):
    a, b = 0, 1
    count = 0
    while count < max_terms:
        yield a
        a, b = b, a + b
        count += 1

# Using the generator
fib_gen = fibonacci_generator(10)

# Print the first 10 Fibonacci numbers
for number in fib_gen:
    print(number)