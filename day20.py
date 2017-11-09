#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

totalSwaps = 0
for i in range(n):
	swapCounter = 0
	for j in range(n-1):
		if(a[j] > a[j+1]):
			a[j],a[j+1] = a[j+1],a[j]
			swapCounter = swapCounter+1
			totalSwaps = totalSwaps+1

	if(swapCounter == 0):
		break

print('Array is sorted in '+str(totalSwaps)+ ' swaps.');
# print('swapCounter = '+str(totalSwaps))	
print('First Element: '+str(a[0]))
print('Last Element: '+str(a[-1]))
