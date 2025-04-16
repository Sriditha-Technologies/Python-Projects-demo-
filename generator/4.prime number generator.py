def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Using the generator
prime_gen = prime_generator()

# Print the first 10 prime numbers
for _ in range(10):
    print(next(prime_gen))