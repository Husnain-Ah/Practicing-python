num1 = float(input('enter your first number : '))
func = input('enter your function from the following : +, -, *, / ')
num2 = float(input('enter your second number : '))

#def is for defining functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


if func == '+':
    print(num1, " + ", num2, " = ", add(num1, num2) )

elif func == '-':
    print(num1, " - ", num2, " = ", subtract(num1, num2) )

elif func == '*':
    print(num1, " * ", num2, " = ", multiply(num1, num2) )

elif func == '/':
    print(num1, " / ", num2, " = ", divide(num1, num2) )

else:
    print("You did not input a correct value")