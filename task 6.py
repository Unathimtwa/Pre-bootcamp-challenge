
def max_of_three_numbers(n1, n2, n3):
    if n1 < n2 < n3:
        print(n3)
    elif n1 < n2 > n3:
        print(n2)
    else:
        print(n1)
    return max_of_three_numbers(n1, n2, n3)

(max_of_three_numbers(2, 12, 6))

