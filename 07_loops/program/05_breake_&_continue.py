for i in range(100):
    if(i == 3.1):
        break #exit the loop right now..abruptly breake the loop 
    print(i)

# when loop is exausted else is used it only usefull when you use breake
# if the no was not found it will executed

else:
    print("not found")

for i in range(100):
    if(i == 31):
        continue # skip this iteration = 1 = somevalue = 1
    print(i)