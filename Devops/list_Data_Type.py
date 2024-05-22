student = ["Tushar","Vishwa","Pantheon","Yasuo","Akali"]

List2 = list(student)
print(List2)

list3 = list("Student")
print(list3)


# Tuple List accessing
champs = ("Pantheon","viego","Tyrndamere","Ezreal")

list4 = list(champs)
print(list4)

stats = list(("Attack",60, "Defence",60))
print(stats)


# Accessing the List Element 
L1 = [1,3,9,2,5,6,7]
print(L1[0])
print(L1[-2])


# Adding Element into the List
# at the end
arr=[3,2,1,5,9]
arr.append(11)
print(arr)

arr.insert(3,36)
print(arr)

l11 = [1,2]
l12 = ["yasuo","Ezreal"]
l11.extend(l12)

print(l11)

# Removing the element
arr = [3,1,5,9,36,3]
arr.remove(3)
print(arr)

arr.remove(3)

# using Pop function
print(arr.pop(3))
print(arr)


# replace the elements 
students = ['a','b','c','d', 'e']
students[3] = 'f'
print(students)


students = ['a','b','c','d','e']
students[1:4] = 'm''n''o'
print(students)

students = ['a','b','c','d','e']
students[1:4] = 'm''n'
print(students)

# To reverse the element of the array 
l1 = [1,2,3,4,5,6,7,8,9]
l1.reverse()
print(l1)

# To copy the elements of the array to another variable with different Memory address
l1 = [1,2,3,4,5,6,7,8,9]
l1_copy = l1.copy()
print(l1_copy)
print(id(l1),id(l1_copy))

