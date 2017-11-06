testCase = int(input())
# oldString = input()
strings = list()
i = 0
# we accept all the stings
for i in range(testCase):
	currentString = input()
	strings.append(currentString)

for i in range(len(strings)):
	# print(strings[i])
	counter = 0
	thisString = strings[i]
	# print(thisString)
	evenStr = ''
	oddStr = ''
	for counter in range(len(strings[i])):
		if(counter % 2 == 0):
			evenStr = evenStr + thisString[counter]
		else:
			oddStr = oddStr + thisString[counter]
	print(evenStr+ ' '+ oddStr)
