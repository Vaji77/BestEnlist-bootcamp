# simple calculator app with try and except for all use cases

def calculator():

    try:

        print('+')
        print('-')
        print('*')
        print('/')
        print('%')
        print('**')
        operation = input("Select an operator:")
        print("Enter two numbers")
        num1 = int(input())
        num2 = int(input())
        if operation == '+':
            print("sum=",num1 + num2)
        elif operation == '-':
            print("diff=",num1 - num2)
        elif operation == '*':
            print("mul=",num1 * num2)
        elif operation == '/':
            print("div=",num1 / num2)
        elif operation == '%':
            print("mod=",num1 % num2)
        elif operation == '**':
            print("pow=",num1 ** num2)
        else:
            print("Invalid Input")
    except Exception as e:
        print("error=",e)
calculator()

# Printing one message if NameError is raised and another for other errors
try:
    c = 10
    print("Value=", c)
    print("Value=", a)
except NameError:
    print("Variable is not defined:Name Error")
except Exception as e:
    print("Other error:", e)

# When try-except scenario is not required?
# Python Exceptions are error scenarios that alter the normal execution flow of the program.
# Try catch is needed only if expected error is small and does not affect the program, in case of fatal errors try catch block is not recommended


# Getting input inside try catch block
try:
    age = int(input('Enter your age: '))
except Exception as e:
    print('You have entered an invalid value:', e)
finally:
    print("Try And Exception are finished")