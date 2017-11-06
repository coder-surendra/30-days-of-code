import sys

string = ''
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for i in range(n):
    string = string + str(arr[0-i-1])
    string = string + ' '
print(string)
