
def max_of_three_numbers(n1, n2, n3):
    if n1 < n2 < n3:
        return n3
    elif n1 < n2 > n3:
        return n2
    else:
        return n1

print(max_of_three_numbers(2, 12, 6))

