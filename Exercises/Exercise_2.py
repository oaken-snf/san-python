# x= input ("What is the number you would like to check?")
# x= int(x)
# y= x-1
# prime= False
# while y>1:
#     if x%y==0:
#         prime= True
#     y=y-1

# if prime==False:
#     print ("Your number is prime.")
# if prime== True:
#     print ("Your number is not prime.")

def listgenerator (integer):
    import random
    list= []
    while integer>0:
      r= random.randint (1,100) 
      list.append (r)
      integer= integer-1
    return (list)


def largest (list):
    s= 0
    for a in list:
     if a>s:
        s=a
    return s

def smallest (list):
    f= largest(list)
    for d in list:
     if d<f:
        f=d
    return f

# small= smallest ([1,2,3,4,5])
# print (small)

def reverse (list):
    otherlist= []
    while len (list) >0:
        otherlist.append (list[len (list)-1])
        list.pop (len (list) -1)
    return otherlist

# rev= reverse ([1,4,2,7,6])
# print (rev)

def alternativelist (list1, list2):
   finallist= []
   while len(list1)> 0 and len(list2)> 0:
    finallist.append (list1[0])
    list1.pop (0)
    finallist.append (list2[0])
    list2.pop (0)
   return (finallist)


# def fibonacci (integer):
#    number1 = 0
#    number2= 1
#    limit = 0
#    while limit < integer:
#        print(number1)
#        nth = number1 + number2
#        number1 = number2
#        number2 = nth
#        limit = limit +1

# fibonacci (7)

# def stringrev (string):
#     otherlist= []
#     for x in string:
#         otherlist.append (x)
#     nextlist= []
#     while len (otherlist) >0:
#         nextlist.append (otherlist[len (otherlist)-1])
#         otherlist.pop (len (otherlist) -1)
#     string= ''
#     for y in nextlist:
#         string= string+y
#     print (string)

# stringrev ("Hello")

# def integerlist (integer):
#      integer= str(integer)
#      list= []
#      for x in integer:
#          list.append (x)
#      print (list)

# integerlist (1234)


# def intergerlist2 (integer):
#     list= []
#     while integer >0:
#         list.append (integer%10)
#         integer= (integer- integer%10) /10
#     print (list)

# intergerlist2 (321)

def palindromechecker (string):
    otherlist= []
    for x in string:
        otherlist.append (x)
    nextlist= otherlist.reverse
    if nextlist == otherlist:
        print ("Your string is a palindrome")
    else :
        print ("Your list is not a palindrome")
    

palindromechecker ("mum")