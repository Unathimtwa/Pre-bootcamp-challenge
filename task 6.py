number1 = input("enter first number: ")
number2 = input("enter second number: ")
number3 = input("enter third number: ")

if number1 < number2 < number3:
    print(number3)
elif number2 < number1 < number3:
    print(number1)
elif number3 < number1 < number2:
    print(number2)
elif number1 > number2 < number3:
    print(number1)

