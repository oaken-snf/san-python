def sayhello (fname, lname):
    print ("Hello" ,fname, lname,"!")

def sum (list):
    total= 0
    for l in list:
        total= total +l
    return total

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

def mean (list1):
    m= 0
    for x in list1:
        m= m+x
    return m/ (len(list1)) 

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

