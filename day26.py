actualDate =  list(map(int, input().strip().split(' ')))
expectedDate =  list(map(int, input().strip().split(' ')))

da = actualDate[0]
ma = actualDate[1]
ya = actualDate[2]

de = expectedDate[0]
me = expectedDate[1]
ye = expectedDate[2]
fine = 0

if ya > ye:
    fine = 10000
else:
    if ya == ye:
        if ma > me:
            fine = 500 * (ma - me)
        else:
            if ma == me:
                if da > de:
                    fine = 15 * (da - de)
            
print(fine)
