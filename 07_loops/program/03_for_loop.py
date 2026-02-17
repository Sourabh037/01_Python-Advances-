# it similar to while loop
# this loop will go from 0 to 4 like in slicing 
# the only difference is you use comma

for i in range(4):
    print(i)
for i in range(0,10,2):
    print(i)

n = int(input("enter a number : "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")