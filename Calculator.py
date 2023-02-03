num1 = int(input('Enter 1st no'))
opr = input('Enter operator +,-,*,/')
num2 = int(input('Enter 2nd no'))
if opr == '+':
    print(num1 + num2)
elif opr == '-':
        print(num1 - num2)
elif opr == '*':
    print(num1 * num2)
elif opr == '/':
    print(num1 / num2)
else:
    print('Invalid operation')