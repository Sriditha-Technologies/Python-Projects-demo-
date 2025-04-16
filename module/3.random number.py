import random
def generate_random_number(start, end):
    return random.randint(start, end)
for _ in range(5):
     print("Random Number: ", generate_random_number(1, 100))