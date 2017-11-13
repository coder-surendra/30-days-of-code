#!/bin/python3

import sys
pattern = '@gmail.com'
myArray = []
N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if pattern in emailID:
        myArray.append(firstName)

myArray.sort()
for i in range(len(myArray)):
	print(myArray[i])
