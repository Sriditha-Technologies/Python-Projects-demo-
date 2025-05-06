def reverse_star_pattern(n):
    for i in range(n, 0, -1):
        print('*' * (2 * i - 1)).rstrip()

# Set number of rows
rows = 5
reverse_star_pattern(rows)