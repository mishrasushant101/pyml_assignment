num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
op = input("Enter the operation that is to be performed eg:- +,-*,/ :")
if op == '+':
    sum = num1 + num2
    print("The sum of two numbers is:",sum)
elif op == '-':
    sub = num1 - num2
    print("The difference of two numbers is:",sub)
elif op == '*':
    mul = num1*num2
    print("The multiplication of two numbers is:",mul)
elif op == '/':
    div = num1/num2
    print("The division of two numbers is:",div)
else:
    print("Input error")