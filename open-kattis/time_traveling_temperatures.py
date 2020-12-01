# https://open.kattis.com/problems/temperature
x, y = input().split(' ')
x = int(x)
y = int(y)

if (x == 0 and y - 1 == 0):
    print("ALL GOOD", end='')
elif (x != 0 and y - 1 == 0):
    print("IMPOSSIBLE", end='')
else:
    if (x % (1 - y) == 0):
        print(x // (1 - y), end='')
    else:
        print("%f" % (x/(1-y)), end='')
