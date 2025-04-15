# Multiplication Table Generator
def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} x {i}={n*i}")


#get user input
number=int(input("Enter the multiplication table of the number is:"))
multiplication_table(number)