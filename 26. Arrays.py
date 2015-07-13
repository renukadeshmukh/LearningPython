
friends = ['Prachi', 'Geetika', 'Shravan']

visited = ['San Fran', 'Santa Clara - El Camino' , 'Santa Cruz', 'Sausolito']

for i in friends :
	print i
	
print "\n"

for i in visited :
	print i
	
print "\n"
print "Third item in list friends is :: ", friends[2]
print "\n"
print "Length of list friends is :: ", len(friends)
print "\n"
print "Length of list visited is :: ", len(visited)

print "\n"

list1 = [1,2,3,4]
list2 = [5,6,7,8]

concatlist = list1 + list2
print concatlist

print concatlist[1:3]

print "\n"
list1.append(0)
print list1

print "\n"
list1.sort();
print list1