numbers = []
a = 1

while a < 1000:
    if a % 3 == 0:
        numbers.append(a)
    elif a % 5 == 0:
        numbers.append(a)
    a += 1

print(sum(numbers))






