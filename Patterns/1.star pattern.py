def star_pattern(n):
    for i in range(n):
         print(' ' * (n - i - 1) + '*' * (2 * i + 1))

rows=5
star_pattern(rows)
