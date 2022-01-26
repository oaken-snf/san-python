# import random
# x= input("What is your number?")
# x= int(x)
# list= []
# while x>0:
#     r= random.randint (1,100) 
#     list.append (r)
#     x= x-1
# print(list)
# list2= []
# x= x-1
# for f in list:
#   list2.append(list[x])
#   x= x-1

# print (list2)


# txt = "The price is {price} dollars"
# print (txt.format (price=49))

# quantity= 3
# itemno= 567
# price=49
# myorder= "I want {} pieces of item number {} for {:.2f} dollars"
# print (myorder.format (quantity, itemno, price))


# age= 36
# name= "John"
# txt= "His name is {1}. {1} is {0} years old."
# print (txt.format (age, name))

import random
list= ["Tin", "Em", "Me", "Bo",]
x=0
while x < 10:
 r= random.randint (0,3)
 print (list [r])
 x= x+1