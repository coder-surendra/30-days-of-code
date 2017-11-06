import sys


n = int(input().strip())
lastRemainder = 0
thisRemainder = 0
myList = []
count = 0
while(n>0):
    thisRemainder = n%2
    print (thisRemainder)
    n = n//2
    if(thisRemainder == 1 and lastRemainder == 1):
        # print('we inside the conditiion')
        count = count + 1
    elif (thisRemainder == 1 and lastRemainder ==0):
        count = 1
    else:
        myList.append(count)
        count = 0
    lastRemainder = thisRemainder
    
myList.append(count)
print(myList)

print(max(myList))