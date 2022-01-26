import random 
n= input ("What is your number?")
n= int(n)
s= []
while 1<n+1:
    r= random.randint (1,100)
    s.append (r)
    n= n-1
print (s)

f= 0
for x in s:
    if x>f:
        f=x
print (f)
