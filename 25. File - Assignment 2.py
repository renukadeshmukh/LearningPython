# Write a program that prompts for a file name, then opens that file and reads through 
# the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and 
# compute the average of those values and produce an output as shown below.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.

filename = raw_input("Enter file name ::")

fhand = open(filename)
count = 0
sum = 0.0

for line in fhand :
	if "X-DSPAM-Confidence" in line :
		num = line[line.find(' '):]
		number = float(num)
		count = count + 1
		sum = sum + number
		
average = sum / count

print "Average spam confidence:", average