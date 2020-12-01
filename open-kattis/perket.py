# https://open.kattis.com/problems/perket
import itertools
num = int(input())
greds = []
for i in range(num):
    pair = input().split(' ')
    greds.append((int(pair[0]), int(pair[1])))

current_min = 1000000000

# single ingredients
for g in greds:
    if abs(g[0] - g[1]) < current_min:
        current_min = abs(g[0]-g[1])

subset = [n for n in range(num)]
for i in range(2, num+1):
    l = list(itertools.combinations(subset, i))
    for s in l:
        sour = 1
        bitter = 0
        for x in s:
            sour = sour * greds[x][0]
            bitter += greds[x][1]
        if abs(sour - bitter) < current_min:
            current_min = abs(sour - bitter)
print(current_min)
