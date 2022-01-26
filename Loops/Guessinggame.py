import random
r= random.randint (1,10)
n= input("What is your guess?")
n= int(n)
numberofattmepts = 1
if n==r:
    print ("You win!!!")
while n!= r and numberofattmepts<=3:
    print ("That is not correct! Try again!!!")
    n = input ("What is your next guess?")
    n = int(n)
    numberofattmepts= numberofattmepts + 1
    if n == r:
      print ("You win! Finally...")
    if numberofattmepts > 3:
        print ("You're out of attempts. Soz!")
   


