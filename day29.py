#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    if ((k-1) | k >n) and k %2 == 0:
        print(k -2)
    else:
        print(k -1)