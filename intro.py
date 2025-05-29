# Basic Calculator Program

#Ask user to input two numbers and the operation

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Enter an operation(+,-,*,/):")

#Perform the operation and display the result
if operation == '+':
    result = num1 + num2
    print(f"{num1}+{num2}={result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1}-{num2}={result}")
elif operation == '*' :
    result = num1 * num2
    print(f"{num1}*{num2}={result}")
elif operation == '/' :
    if num2 != 0:
      result = num1/num2
      print(f"{num1}/{num2}={result}") 
    else :
        print("Error: Cannot divide by zero.")
else :
    print("Invalid operation. Please use +,-,*, or /.")
                     
    
