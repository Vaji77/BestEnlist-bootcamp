# 1.python script to merge two dictionaries

dict1 = {"kerala":"trivandrum","goa":"panji","madhya pradesh":"bhopal","karnataka":"banglore","up":"bihar"}
dict2 = {"japan":"tokyo","china":"shanghai","india":"newdelhi","australia":"sydney","pakistan":"lahore"}
print("dict1=",dict1)
print("dict2=",dict2)
dict3 =dict1.copy()
for key,value in dict2.items():
    dict3[key] = value
print("merged dict=",dict3)

# 2.remove a key from dictionaries
dict4={"kerala":"trivandrum","goa":"panji","madhya pradesh":"bhopal"}
print("dict4=",dict4)
dict4.pop("kerala")
print("dict after removing=",dict4)


# 3.program to map two list into dictionary
lst1 = []
lst2 = []
n = int (input("enter the number of elements for dictionaries:"))
print("For keys:")
for x in range(0,n):
    element = input("enter element" + str(x+1) + ":")
    lst1.append(element)
print("For values:")
for x in range(0,n):
    element = input("enter element" + str(x + 1) + ":")
    lst2.append(element)
d = dict(zip(lst1,lst2))
print("the dictionary is:",d)

# 4.program to find length of set
dict5 = {"vaji":5,"aji":6,"alwin":8,"joel":9}
print("dict 5=",dict5)
print("length of set:",len(dict5))

# 5.removing intersection of 2nd set from 1st set:
print("removing intersection of 2nd set from 1st set:")
s1 = {1,2,3,4,5}
s2 = {2,3,7,6,4}
print("original set:")
print(s1,"\n",s2)
s1.difference_update(s2)
print("set 1 : ", s1)
print("set 2 :", s2)