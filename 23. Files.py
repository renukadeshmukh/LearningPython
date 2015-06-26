
fhand = open('SeverusSnape.txt')

print fhand, "\n\n"

#read and print file
for line in fhand :
	print line
	
	
# count number of lines in file
fhand = open('SeverusSnape.txt')

count = 0
for line in fhand :
	count = count + 1
	
print "\n\nTotal number of lines in this file is", count


#length of file
fhand = open('Hedwig.txt')
text = fhand.read()
length = len(text)
print "\n\nLength of text is", length