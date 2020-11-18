num1 = int(input("please enter a number: "))
num2 = int(input("please enter another number: "))

if num1 == 3 or num2 == 3 and (num2 + num1) // 3 == 0:
    print(True)
else:
    print(False)

