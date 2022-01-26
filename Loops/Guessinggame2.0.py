import random
r= random.randint (1,100)
n= input("What is your guess?")
n= int(n)
if n==r:
    print ("You win!!!ON THE FIRST TRY!!!!")
while n!= r:
    if n > r :
        print ("That is too high! Try again!!!")
    if n < r :
        print ("That is too low! Try again!")
    n = input ("What is your next guess?")
    n = int(n)
    if n == r:
      print ("You win! Finally... jk! Good job!")