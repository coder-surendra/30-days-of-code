#!/bin/python3

import sys


S = input().strip()
try:
    myNum = int(S)
    print(myNum)
except:
    print('Bad String')