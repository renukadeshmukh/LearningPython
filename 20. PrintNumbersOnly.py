# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 
# 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user 
# enters anything other than a valid number catch it with a try/except and put out an appropriate 
# message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the 
# desired output as shown.


largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" :
		print "Maximum is", largest
		print "Minimum is", smallest
		break
    else :
		try:
			iNum = int(num)
			if largest is None : 
				largest = iNum
			elif iNum > largest :
				largest = iNum
				
			if smallest is None : 
				smallest = iNum
			elif iNum < smallest :
				smallest = iNum
			
		except :
			print "Invalid input"
			continue
    

