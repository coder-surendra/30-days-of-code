dictionary = dict()
n = int(input())
for i in range(n):
    k,v = input().strip().split(' ')
    dictionary[k] = v

arr = []
j = 0
for j in range(n):
	name = input()
	if name in dictionary:
		number = dictionary[name]
		print(name + '='+str(number))
	else:
		print("Not found")
