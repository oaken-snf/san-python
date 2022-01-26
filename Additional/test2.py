twonumbers= input ("Please enter two numbers seperated by space")

results = twonumbers.split (" ")
number1= int(results[0])
number2= int(results[1])

thing= "Your first number is {} and your second number is {}"
print (thing.format (number1,number2))