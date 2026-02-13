# list are mutable unlike string..we can change the data in list
# in list data are store in [] formate

friend = ["apple", "orange", 5, 345.06, False, "akash", "rohan"]
print(friend[0])

friend[0] = "grapes" 
print(friend[0])

# how to input data in list or other sets 
# there are no data in list to use insert

fruits = []
f1 = input("enter a fruit : ")
f1.append(f1)
f2 = input("enter a fruit : ")
f1.append(f2)
f3 = input("enter a fruit : ")
f1.append(f3)
f4 = input("enter a fruit : ")
f1.append(f4)
f5 = input("enter a fruit : ")
f1.append(f5)

print(fruits)