
x = 10

while x >= 0:
	print x
	x = x - 1

print "All Done"

for i in [5,4,3,2,1,0] :
	print "In for loop ", i, "times"
print ""
print ""


print "Max number is ::"	
# find the largest number from array
arr = [54, 76, 48, 40, 7, 98, 24, 18]
max = arr[0]
for i in arr : 
	if i >= max :
		max = i
		
print max
print ""
print ""

print "Sum of array numbers is ::"	
# find the sum of number from array
sum = 0
for i in arr : 
	sum += i
		
print sum

print ""
print ""

print "Numbers greater than 40 are ::"	
# find the sum of number from array
for i in arr : 
	if i > 40 : 
		print i
		
print "\n\n"
smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print smallest_so_far	