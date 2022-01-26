pricetag = []

houseprice = open('house_price.txt', 'r')
Lines = houseprice.readlines()
for x in Lines:
    y= int (x.replace("\n", ""))
    pricetag.append(y)
#print (pricetag)

#s= 0
#for a in pricetag:
 #   if a>s:
  #      s=a
#print (s)

#f= 990000
#for d in pricetag:
#    if d<f:
 #       f=d
#print (f)

sum= 0
for l in pricetag:
    l= l/10
    sum= sum+l
print (sum)
    