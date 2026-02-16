# this is called if elif else ladder
a = int(input(" Enter a number : "))

# blank space after condition = indentation means we are inside a condition
if(a>=18)
    print("you are above the age of consent")
elif(a<0):
    print("you are enterning an invalid age")
elif(a==0):
    print("you are enterning 0 which is not a valid age")
else:
    print("you are belove the age of consent")