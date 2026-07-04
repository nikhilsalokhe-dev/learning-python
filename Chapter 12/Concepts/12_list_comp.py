myList = [1, 2, 3, 4, 5, 6]

sqauredList = []

# for item in myList:
#     sqauredList.append(item * item)

# This can be simplified using list comprehensions

sqauredList = [i * i for i in myList]

print(sqauredList)

# Another example

list1 = [1, 7, 12, 11, 22]
list2 = [item for item in list1 if item > 8]
print(list2)
