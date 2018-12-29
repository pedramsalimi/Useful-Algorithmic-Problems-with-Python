def sum_of_digits(n):
    if n%10 == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n-1)

print(sum_of_digits(12345))
