def number_triangle(n):
    for i in range(1,n + 1):
        print(" ".join(str(num)for num in range(1,i + 1)))

rows=5
number_triangle(rows)
