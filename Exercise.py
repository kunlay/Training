# name = input("what is your name? \n")
# age = int(input("how old are you? \n"))
# year = str((2017 - age)+100)
# print(name + " you will be 100 in " + year + " years")
# new_number = int(input("enter a new number? \n"))
# year = str((2017 - new_number)+100)
# print((name + " you will be 100 in " + year + " years" '\n' ) * 4)


viewer = int(input("enter age? \n"))
if viewer > 17:
    print("can see a rated R movie")
elif viewer < 17 and viewer > 12:
    print("can see a rated PG-13 movie")
else:
    print("can only see rated PG movies")