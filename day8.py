# 1.python script to merge two python dictionaries

dict1 = {1 : 'a', 2 : 'b', 3:'c', 4 :'d'}
dict2 = {5 :'e',6 :'f',7 :'g'}
dict3 = {**dict1, **dict2}
print(dict1)
print(dict2)
print(dict3)

# 2. program to sort value from descending to ascending in list and convert to set

list1 = [100,90,80,70,60,50]
print("descending order list =",list1)
list1.sort()
print("sorted list from descending to ascending:\n",list1)
x = set(list1)
print("converting list into set:\n",x)

# 3.program to list no of item in dictionary and sort it with and without using function

y =[]
unsorted_list=[]
sorted_list=[]
d = {'dhoni':36,'jaddu': 30,"kohli":32,"sachin":50}
for i in d.keys():
    y.append(i)
    unsorted_list.append(i)
y.sort()
print("using function\n",y)

# sorting list without using function
while unsorted_list:
    minimum = unsorted_list[0]
    for j in unsorted_list:
        if j < minimum:
            minimum = j
    sorted_list.append(minimum)
    unsorted_list.remove(minimum)
print("without using function")
print(sorted_list)

# 4.program to take string as input and  change the first occurence with user input


inp = input("enter the string :\n")
inp2 = input("enter the character that has to be change with first word:\n")
newstring = inp.replace(inp[0], inp2,1)
print("new string=",newstring)

# 5.program to take string as input and change all the occurence  of the first character have been changed to capital letter

inp3 = input("enter string :\n")

replacedword = inp3.capitalize()
print("replaced word=",replacedword)

# 6.program to find the repeated elements in the list

inp5 = ["a","b","c","f","e","a","c","f","a","b","d","e"]
print("input elements =",inp5)
inp6 = []
inp7 = []
for i in inp5:
    if i not in inp6:
        inp6.append(i)
    elif i not in inp7:
        inp7.append(i)
    else:
        None
print("the repeated elements are:", inp7)

# 7.program to check the sum of  three elements and divide it by value given by the user

a = 10
b = 20
c = 30
sum = a+b+c
print("sum of the numbers =",sum)
inp8= int(input("enter the number  to divide the sum:\n"))
print("result =:\n",sum/inp8)

# 8.program to find the mean,median,mode

#mean

list1=[8,2,2,2,4,6]                                                   # three given numbers
list2 = list1
addition = 0
for q in list1:
    addition = addition +q
print("sum=",addition)
length = len(list1)
mean = addition/length
print("mean:",mean)
#median
list2.sort()
n = len(list2)
if n % 2 ==0:

    median = length/2
else:
    median = list2[n // 2]
print("median is:"  + str(median))
#mode
mode1 = list1
mode1.sort()
l1=[]

i = 0
while i < len(mode1):
    l1.append(mode1.count(mode1[i]))
    i += 1

mode2 = dict(zip(mode1 , l1))

mode2 = {k for (k,v) in mode2.items() if v== max(l1)}

print("Mode is =" + str(mode2))

# 9.Python program to swap cases of a given string

a = "Hello"
b = "World"
temp = a
a = b
b = temp
print(a,b)
x = a
y = b
x, y = y, x
print(x,y)

# 10.program to convert an integer to binary & octa decimal

def deciToOctal():
    n = int(input("enter the decimal value:"))
    print("decimal value is:",n)
    octalnum = [0] * 100
    i = 0
    print("octal number is:")
    while (n != 0):
        octalnum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(octalnum[j], end="")
deciToOctal()


