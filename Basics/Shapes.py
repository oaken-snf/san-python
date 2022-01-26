shape= input ("What is your shape?")
if shape != "circle" and shape!= "rectangle" and shape!= "square" and shape!= "triangle":
    print ("Sorry, your shape is not valid. Try again but don't use capital letters. Make sure it is a circle, recatangle, triangle or square!")
if shape == "circle":
    radius = input ("What is the radius of your circle in cm?")
    radius = int(radius) 
    print ("The area of your cicle is" ,radius**2 * 3.14, "cm and the circumference of your circle is" ,radius * 2* 3.14, "cm")
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