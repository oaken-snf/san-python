x = input ("What is your number?")
x = int(x)
a = x%6
if a==0:
    print ("Your number can divide by 6. At least you know maths." )
if a!= 0:
    print ("Your number is not divisible by 6. Too bad.")