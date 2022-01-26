x = input ("What is your number?")
x = int(x)
i = 2
isPrime = True
while i < x:
    if x%i == 0:
        isPrime = False
        break
    i= i+1

if isPrime:
   print ("Your number is prime")
else :
    print (x, "is not prime")
