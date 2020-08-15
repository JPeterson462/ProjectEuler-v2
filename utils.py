import math

def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n = int(n / 10)
    return rev

def count_digits(n):
    return int(math.log10(n)) + 1