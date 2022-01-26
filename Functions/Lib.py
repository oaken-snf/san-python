def san (name):
    print ("Hello", name )

def sayhello (fname, lname):
    print ("Hello" ,fname, lname,"!")

def multiply_by_5 (number):
    print (number * 5)

def two_numbers (number1, number2):
    print (number1 * number2)

def sum (listofitems):
     total= 0
     for l in listofitems:
       total= total+l
     return total

def max (list):
    s= 0
    for a in list:
     if a>s:
        s=a
    return s
    
    
def min (list):
    f= max(list)
    for d in list:
     if d<f:
        f=d
    return f

def mean (list):
    m= 0
    for s in list:
        m= m+s
    return m/ (len(list)) 

def fth (list, item):
    if item in list:
        return (True)
    if item not in list:
        return (False)

def reverse (list):
    list.sort (reverse = True)
    print (list)

def odd (list):
    result= []
    for l in list:
        if l%2 != 0:
          result.append (l)
    return (result)

def twolists (list1, list2):
    final= []
    for x in list1:
        final.append (x)
    for y in list2:
        final.append (y)
    return (final)

def primechecker (number):
     isPrime= True
     x= 2
     while x<number:
        if number % x == 0:
            isPrime= False
        x= x+1
     return isPrime


def alternativelist (list1, list2):
   final= []
   while len(list1)> 0 and len(list2)> 0:
    final.append (list1[0])
    list1.pop (0)
    final.append (list2[0])
    list2.pop (0)
   return (final)
   
def collatz (number):
    while number!= 1:
        if number%2==0:
            number= number/2
        else:
            number= (3* number) +1
    print (number)

def mean (list):
    m= 0
    for s in list:
        m= m+s
    return m/ (len(list)) 

def random (int):
    import random
    r= random.randint (1,100)   
    return (r)

def percirc (int):
    perimeter=2*3.14*int
    print (perimeter)

def areacirc (int):
    area= int*int*3.14
    print (area)

def listgenerator (integer):
    import random
    list= []
    while integer>0:
      r= random.randint (1,100) 
      list.append (r)
      integer= integer-1
    return (list)

def findmax (list1):
    list1.sort(reverse=True)
    return(list1[0])

def oddspace (list2):
    resultlist= []
    length= len(list2)
    i= 1
    while i<length:
        resultlist.append (list2[i])
        i= i+2
    return (resultlist)

def shapesy (shape):
   if shape != "circle" and shape!= "rectangle" and shape!= "square" and shape!= "triangle":
    print ("Sorry, your shape is not valid. Try again but don't use capital letters. Make sure it's either a circle, rectangle, triangle or square!")
   if shape == "circle":
    radius = input ("What is the radius of your circle in cm?")
    radius = int(radius) 
    print ("The area of your circle is" ,radius**2 * 3.14, "cm and the circumference of your circle is" ,radius * 2* 3.14, "cm")
   if shape == "rectangle":
    length = input ("What is the length of your rectangle in cm?")
    length = int(length)
    width = input ("What is the width of your rectangle in cm?")
    width= int(width)
    print ("The area of your rectangle is" ,length * width, "cm and the perimeter is" , (length+width) *2, "cm" )
   if shape == "square":
    side = input ("What is the side of your square in cm?")
    side= int(side)
    print ("The area of your square is" ,side **2, "cm and the perimeter of your square is" , side *4, "cm")
   if shape == "triangle":
    height = input ("What is the height of your triangle in cm?")
    height = int (height)
    base = input ("What is the base of your triangle in cm?")
    base = int (base)
    print ("The area of your triangle is" ,height * base /2, "cm")


def rev (list):
    otherlist= []
    while len (list) >0:
        otherlist.append (list[len (list)-1])
        list.pop (len (list) -1)
    return otherlist

def fibonacci (integer):
   number1 = 0
   number2= 1
   limit = 0
   while limit < integer:
       print(number1)
       nth = number1 + number2
       number1 = number2
       number2 = nth
       limit = limit +1

def stringrev (string):
    otherlist= []
    for x in string:
        otherlist.append (x)
    nextlist= []
    while len (otherlist) >0:
        nextlist.append (otherlist[len (otherlist)-1])
        otherlist.pop (len (otherlist) -1)
    string= ''
    for y in nextlist:
        string= string+y
    print (string)

def integerlist (integer):
     integer= str(integer)
     list= []
     for x in integer:
         list.append (x)
     print (list)

def intergerlist2 (integer):
    list= []
    while integer >0:
        list.append (integer%10)
        integer= (integer- integer%10) /10
    print (list)