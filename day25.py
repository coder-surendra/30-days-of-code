import math
N = int(input())
for i in range(N):
    number = int(input())
    j = 2
    isPrime = True
    while(j <= int(math.sqrt(number))):
        if(number%j == 0):
            isPrime = False
            break
        j = j + 1
    if isPrime and number != 1:
        print('Prime')
    else:
        print('Not prime')