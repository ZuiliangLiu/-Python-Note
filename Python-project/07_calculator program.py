# Python calculator

operator = input("Please enter your operator:+ - * / ")

num1 = float(input("Please enter your 1st number:"))
num2 = float(input("Please enter your 2nd number:"))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    result = (num1 / num2)
    print(round(result,3))