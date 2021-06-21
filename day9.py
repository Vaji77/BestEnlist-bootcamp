# 1.program to loop through a list of numbers and add +2 to every value to the elements in list
list1 = [1,2,3,4,5,6,7,8,9]
l = []
n = len(list1)
for i in list1:
    l.append(i+2)
print(l)

# 2. program to print

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

# 3.fibonacci series
n = int(input("enter the number of terms:"))
a = 0
b = 1
count = 0
if n <= 0:
    print("Enter a positive integer")

elif n == 1:
    print("Fibonacci sequence:")
    print(a)

else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        sum = a + b
        a = b
        b = sum
        count += 1
    print()

# 4.amrstrong number
num = int(input("enter the digit to check whether the digit is amstrong or not:"))
sum = 0
temp1 = num
while temp1>0:
    digit = temp1%10
    sum+=digit**3
    temp1//=10
if num == sum:
    print(num,"is amrstrong")
else:
    print(num,"is not amrstrong")

# 5.program to print  multiplication table of 9
num = int(9)
mul = 0
print("multiplication table of 9 is:")
for p in range(1,10+1):
    mul21 = num*p
    print(num ,"x", p ,"=", mul)

# 6.program to find the given number is positive or negative
#print("\n")
num = int(input("Enter a number to check whether the number is positive or negative"))
if num > 0:
    print(num, "is positive")
else:
    print(num, "is negative")

# 7.program to convert the number of days to ages

days = int(input("Enter number of days:"))
yrs = int(days / 365)
print("No of years:", yrs)

# 8.trignometry program using math function

import math

def trig(n, m):
    if n == 'sin':
        print("Sine of ", m, " is", math.sin(m))
    elif n == 'cos':
        print("Cosine of ", m, " is", math.cos(m))
    elif n == 'tan':
        print("Tangent of ", m, " is", math.tan(m))
    elif n == 'sec':
        print("Secant of ", m, " is", (1 / math.cos(m)))
    elif n == 'cosec':
        print("Cosecant of ", m, " is", (1 / math.sin(m)))
    elif n == 'cot':
        print("Cotangent of ", m, " is", (1 / math.tan(m)))

trig("sin", 90)
trig("cos", 90)
trig("tan", 90)
trig("cosec", 90)
trig("sec", 90)
trig("cot", 90)

# 9.basic calculator program

print('calculator')
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

ch = int(input("enter choice(1-4):"))

if ch ==1:
    a =int(input("enter a:"))
    b = int(input("enter b:"))
    c = a+b
    print("sum=",c)
elif ch == 2:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    c = a - b
    print("difference = ",c)
elif ch==3:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    c = a * b
    print("product = ", c)
elif ch==4:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    c = a / b
    print("quotient = ", c)