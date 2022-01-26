print ("Hello! Welcome to Sanmmonwealth Bank!")
n= input ("How much money do you want to deposit?")
n= float (n)
t= input ("What is your target amount?")
t= float(t)
y= 0
while n < t:
    n= 0.05 *n + n
    y= y+1
print ("You will need to keep your money in the bank for" ,y, "years.")