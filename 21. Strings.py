fruit = 'banana'

letter = fruit[1]
print letter

n = 4
w = fruit[n]
print w

print "length of banana is", len(fruit)

index = 0
print ""
print ""
# While loop
print "While loop"
while index < len(fruit) :
	print index , fruit[index]
	index = index +1
	
print ""
print ""
print "For loop"
for i in fruit :
	print i
	
	
print ""
print ""
print "Slicing"
s = "Monty Python"
print s[0:4]
print s[6:7]
print s[6:20]
print s[:2]
print s[8:]
print s[:]


print ""
print ""
print "String Comparison"
if fruit == 'banana' :
	print 'Fruit is banana'
elif fruit == 'orange' :
	print 'Fruit is orange'


print ""
print ""
print "Case Conversion"
greet = "Hello Bob"
print greet
lowerGreet = greet.lower()
print lowerGreet
upperGreet = greet.upper()
print upperGreet
greetJane = greet.replace('Bob' , 'Jane')
print greetJane
x = 'From marquard@uct.ac.za'
print x[8]
print x[14:17]
print len('banana')*7


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print data[pos:pos+3]