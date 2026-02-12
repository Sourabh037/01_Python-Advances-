# now some string function
# the gaps are also consider a charater

name = "i am sourabh"

# used function
print(len(name))
print(name.count("a"))
print(name.find("s"))

# this function is for replace but also a chained
print(name.replace("i am", "am i").replace("sourabh","?"))

# not much used function
print(name.endswith("bh"))
print(name.startswith("so"))
print(name.capitalize())