print ("Hello! Welcome to Sanmmonwealth Bank!")
n= input ("How much money do you want to deposit?")
n= float (n)
y= input ("How many years will you be keeping your money in our bank?")
y= int(y)
while 0 < y:
    n= (0.01*n) + n
    y= y-1
print ("You will have" ,n, "dollars in the bank" )


