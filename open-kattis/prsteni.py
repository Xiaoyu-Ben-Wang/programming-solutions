# https://open.kattis.com/contests/prsteni
def fraction(a, b):
    for i in range(min(a, b), 1, -1):
        if (a % i == 0 and b % i == 0):
            a = a // i
            b = b // i
    return (a, b)


rings = int(input())

radii = input().split(' ')

for i in range(1, rings):
    ratio = fraction(int(radii[0]), int(radii[i]))
    print("%d/%d" % (ratio[0], ratio[1]))
