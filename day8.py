dictionary = dict()
n = int(input())
for i in range(n):
    k,v = input().strip().split(' ')
    dictionary[k] = v

# print(dictionary)
# accept the values for the search names
# arr = []

# flag = True
# while(flag):
# 	name = input()
# 	if(name == ''):
# 		flag = False
# 	else:
# 		arr.append(name)

# print(arr)

# length = len(arr)

# i = 0
# allKeys = dictionary.keys();

# for i in range(length):
# 	findKey = arr[i]
# 	if findKey in allKeys:
# 		print(findKey+'='+dictionary[findKey])
# 	else:
# 		print('Not found')

arr = []
j = 0
for j in range(n):
	name = input()
	if name in dictionary:
		number = dictionary[name]
		print(name + '='+str(number))
	else:
		print("Not found")
