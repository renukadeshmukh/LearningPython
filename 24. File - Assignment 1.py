# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.pythonlearn.com/code/words.txt

filename = raw_input("Please enter filename :: ")

fhand = open(filename)

for line in fhand :
	print line.rstrip().upper()