# x= input ("What is your temperature in degrees celsius?")
# x= int(x)
# print ("In fahrenheit degrees, your temerature is" ,x / 5 * 9 +32, "degrees fahrenheit")


# x= input ("What is the distance between destination A and destination B in km?")
# x= int(x)
# y= input ("What is the speed you are travelling at in km per hour?")
# y= int (y)
# print ("It will take you" ,x /y, "hours.")


# x= input ("What is your number?")
# x= int (x)
# while x>0:
#     if x%6==0:
#         print (x)
#     x= x-1

# print ("Hello! Welcome to Sanmmonwealth Bank!")
# n= input ("How much money do you want to deposit?")
# n= float (n)
# y= input ("How many years will you be keeping your money in the bank?")
# y= int(y)
# i= input ("What is your interest rate (please put into decimals)?")
# i= float (i)
# while 0 < y:
#     n= (i*n) + n
#     y= y-1
# print ("You will have" ,n, "dollars in the bank" )

print ("Hello! Welcome to Sanmmonwealth Bank!")
n= input ("How much money do you want to deposit?")
n= float (n)
t= input ("What is your target amount?")
t= float(t)
i= input ("What is your interest rate in decimals?")
i= float(i)
y= 0
while n < t:
    n= i *n + n
    y= y+1
print ("You will need to keep your money in the bank for" ,y, "years.")