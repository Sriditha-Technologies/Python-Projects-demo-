def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Sequence:")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b  # Update values for next iteration

number_of_terms = int(input("Enter the number of terms in Fibonacci series: "))
fibonacci(number_of_terms)