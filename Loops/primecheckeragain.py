x = input ("What is your number?")
x = int(x)
i = 2
isprime = True
while i < x:
    if x%i == 0:
        isprime = False
        break
    i= i+1

if isprime:
   print ("Your number is prime")
else :
    print ("Your number is not prime")