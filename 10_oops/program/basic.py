class employee:
    #  these are class attribute
    name = "harry"  #----------------------
    language = "py"         #              |
    salary = 120000         #              |
                             #             |
sourabh = employee()          #            |
# name is object instance attribute        |
sourabh.name = "sourabh"       #           |
# first will always be instance attribute--| 
print(sourabh.name, sourabh.language, sourabh.salary)