# https://open.kattis.com/problems/tourdefrance

while True:

    pair = input().split(' ')
    if pair[0] == '0':
        break

    sprockets = [int(z) for z in pair]
    f_teeth = [int(x) for x in input().split(' ')]
    r_teeth = [int(y) for y in input().split(' ')]
    ratios = []
    for i in range(sprockets[0]):
        for j in range(sprockets[1]):
            ratios.append(r_teeth[j] / f_teeth[i])
    ratios.sort()
    spread = []
    for i in range(len(ratios) - 1):
        spread.append(ratios[i+1]/ratios[i])
    spread.sort()
    print("%.2f" % max(spread))