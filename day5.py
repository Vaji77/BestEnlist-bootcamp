# 1.create a program of list of n integer values
n = 20
lst = [x for x in range(0,n)]
print("list = \n",lst)


# add an item in to the list
lst.append(100)
lst.insert(10,50)
print("list after adding an item:\n",lst)


# delete an item
lst.pop(10)
print("list after removing an item:\n",lst)

# largest number
lar = max(lst)
print("largest no is:",lar)

# smallest number
small = min(lst)
print("smallest no is:",small)

# 2.create a tuple and print reverse of the created tuple
tup = (22,25,32,31,28,17,19)
print("tuple:\n",tup)
reverse = tup[::-1]
print("tuple after reversing :\n",reverse)

# 3.create a tuple and convert it into list
tup2 = (7,9,10,11,17,21,77)
list1 = list(tup2)
print("tuple after coverting into list\n:",list1)