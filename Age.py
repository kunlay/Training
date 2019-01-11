
# first_name = input("enter first name \n")
# print(first_name)
# print(first_name[::-1])

# permission = "manager"
# user_level = input("what is your level? \n")
# if user_level == permission or user_level == "senior manager":
#     print("this is the report")


# user_age = input("what is your age? \n")
# user_age = int(user_age) 
# if user_age > 18:
#     print("welcome")


# user_name = input("enter your name? \n")
# user_age = input("enter your age? \n")
# user_age = int(user_age)
# if user_age >= 1960 or user_age <= 2000:
#     print(user_name)
#     print(2018 - user_age)    
    
#continent = input("which continent are you from? \n")
# if continent == "african":
#     print("Yo nigga")
# elif continent == "british":
#     print("yellos")
# else:
#     print("NO MATCH")

# user = int(input("enter a number? \n"))
# if user%2 == 1:
#     print("odd")
# else:
#     print("even")

# user = int(input("enter birth year? \n"))
# age = 2018 - user
# if age < 10:
#     print("welcome to the world")
# elif age > 10 and age <= 20:
#     print("you are just starting")
# elif age > 20 and age <= 40:
#     print("well done, you are getting there!")
# elif age > 40 and age <= 60:
#     print("set for retirement")
# elif age > 60 and age <= 90:
#     print("ENJOY!!, you worked for it")
# elif age > 90 and age <= 120:
#     print("Prepared to GO??")
# else:
#     print("GOOD NIGHT CHALEEE!!!")

# score = int(input("enter your score? \n"))
# if score >= 70 and score <= 100:
#     print("A")
# elif score >= 60 and score <= 69:
#     print("B")
# elif score >= 50 and score <= 59:
#     print("C")
# elif score >= 45 and score <= 49:
#     print("D")
# elif score >= 40 and score <= 44:
#     print("E")
# else:
#     print("F")

# x = 0
# while x <= 10:
#     if x%2 == 0:
#         print("Even")
#     else:
#         print(x)
#     x+=1
    
# print("we are done")

# a = 1
# while a < 10:
#     print(a)
#     if a == 5:
#         break
#     a+=1

# a = 1
# while a < 10:
#     # print(a, "first")
#     a+=1
#     # print(a, 'second')
#     if a == 5:
#         continue
#     print(a)

# name = "adekunle"
# for letter in name:
#      print(letter.upper())


# greetings = ["hello","hi","hey"]
# for word in greetings:
#     my_list = []
#     for letter in word:
#         my_list.append(letter)
#     print(my_list)
    

# my_tuple = (3,5,9) # unique data
# a,b,c = my_tuple
# print(a,b,c)

# my_set = {2,3,2,5,}   # to remove duplicate
# print(my_set)
# my_set.add(7)  #add to a set
# print(my_set)
# my_set.discard(3) #remove from a set
# print(my_set)

# set1 = {"a","b","c"}
# set2 = {"d","e","f","b"}
# union_Set = set1-set2
# print(union_Set)

# union = |
# intersection = &
# difference = -
# for items in itereable:
#     print(items)

# my_list = [1,2,3]
# for items in my_list:
#     print(1 in my_list)


# my_list = [2,4,5]
# new_list = []
# for item in my_list:
#     new_list.append(item*2)
# print(new_list)


# number = [3,4,5,6]
# new_number = []
# for items in number:
#     new_number.append(items*5)
# print(new_number)

# greeting = "Hello"
# # my_tuple = ("vowels")
# # e,o = my_tuple
# e = "vowels"
# for word in greeting:
#     print(word.replace("e","vowels"))
#     # print(word.replace("o", "vowels"))
    
# # my_tuple = (3,5,9) # unique data
# # a,b,c = my_tuple
# # print(a,b,c)

# # print(word.replace("e","o" "vowels"))

# def nextPrime(n):
#     while True:
#         n+=1
#         for i in range(2,n):
#             if n % i == 0:
#                 break
#         else:
#             return n


# mylist = ['mayowa','ade','kunle','kens']
# for i in range(len(mylist)):
#     if i == 2:
#         print(mylist[i])

# mylist = [[1,2],[3,4],[5,6],[7,8]]
# newlist = []
# for i in mylist:
#     newlist2 = []
#     for items in i:
#         newlist2.append(items * 2)
#     newlist.append(newlist2)
# print(newlist)

# mylist = [[1,2],[3,4],[5,6],[7,8]]
# newlist = []
# for i in mylist:
#     for items in i:
#         newlist.append(items ** 2)
# print(newlist)



# cream = [1,2[2,5],[8,9,5],5,6,[2,[3,5]]]
# cream_new = []
# for i in cream:
#     cream_new2 = []
#     for items in i:
#         cream_new3 = []
#         for x in items:
#             cream_new3.append(x * 2)
#         cream_new2.append(cream_new3)
#     cream_new.append(cream_new2)
# print(cream_new)


# import Function
# import Function as f
from Function2 import startPrime
myVar = startPrime(2)
print(myVar)