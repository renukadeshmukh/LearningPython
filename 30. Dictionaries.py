days = dict()
days['Sunday'] = 0
days['Monday'] = 1
days['Tuesday'] = 2
days['Wednesday'] = 3
days['Thursday'] = 4
days['Friday'] = 5
days['Saturday'] = 6


print days['Tuesday']

print days['Saturday'] + 5

print days

ispresent = 'leapyear' in days
print ispresent

ispresent = 'Monday' in days
print ispresent

print days.keys()
print days.values()
print days.items()

for day,indx in days.items() :
	print day, " : " , indx