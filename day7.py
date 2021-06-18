# 1.Function to input two integers from user and perform addition subtraction,division and multiplication
def get():
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    print("Addition of two numbers is", num1 + num2)
    print("Subtraction of two numbers is", num1 - num2)
    print("Division of two numbers is", int(num1 / num2))
    print("Multiplication of two numbers is", num1 * num2)

get()

#2. create function covid() & it should accept patient name,and body temperature,by default the body temperature should be 98 degree
def covid(a,b):
    print("patient name is:", a, "\tbody temperature is:", b)
a = input("enter patients name:\n")
c = input("enter patients temperature :\n")
if c.isspace() == True:
    b = 98
else:
    b = c
covid(a,b)
