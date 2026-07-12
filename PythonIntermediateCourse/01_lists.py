# list - ordered, mutable, allows duplicate elements

# Copying a list

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

list2 = list1

list1.append(10)

print(list1)
print(list2)


list3 = [x * x for x in list2]

print(list3)
