# Now how to do slice in a string 
# In string every character has an index
# which is like if you start form 'S' index = 0,1,2....
# and if you start from last 'h' index = -1,-2,....
# [0:6:-1\-2]     steps
#         |_________|

#       0123456
name = "Sourabh"
#      -7654321 

#  Length...
print(len(name))

# positive...
print(name[0:5])

# nagitive...
print(name[-2:-7:-1])

# Empty...if you write one side empty python will consider as the last index
print(name[:6])
print(name[2:])

# Combine...
print(name[-3:1:-1])
print(name[::-2])