# Basic Calculator Program

#Ask user to input two numbers and the operation

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Enter an operation(+,-,*,/):")

#Perform the operation and display the result
if operation == '+':
    result = num1 + num2
    print(f"{num1}+{num2}={result}")