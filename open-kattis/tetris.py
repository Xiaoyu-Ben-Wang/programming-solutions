# https://open.kattis.com/problems/tetris
dim = input().split(' ')
C = int(dim[0])
P = int(dim[1])
h = [int(x) for x in input().split(' ')]
total = 0
if P == 1:
    total += C
    for i in range(C - 3):
        if h[i] == h[i + 1] and h[i + 1] == h[i + 2] and h[i+2] == h[i+3]:
            total += 1
elif P == 2:
    for i in range(C - 1):
        if h[i] == h[i + 1]:
            total += 1
elif P == 3:
    for i in range(C - 2):
        if h[i] == h[i + 1] and h[i + 1] == h[i + 2] - 1:
            total += 1
    for i in range(C - 1):
        if h[i] - 1 == h[i + 1]:
            total += 1
elif P == 4:
    for i in range(C - 2):
        if h[i]-1 == h[i + 1] and h[i + 1] == h[i + 2]:
            total += 1
    for i in range(C - 1):
        if h[i] == h[i + 1]-1:
            total += 1
elif P == 5:
    for i in range(C - 2):
        if h[i] == h[i + 1] and h[i + 1] == h[i + 2]:
            total += 1
        if h[i] - 1 == h[i + 1] and h[i + 1] == h[i + 2]-1:
            total += 1
    for i in range(C - 1):
        if h[i] == h[i + 1] + 1:
            total += 1
        if h[i] + 1 == h[i + 1]:
            total += 1
elif P == 6:
    for i in range(C - 2):
        if h[i] == h[i + 1] and h[i + 1] == h[i + 2]:
            total += 1
        if h[i] == h[i + 1] - 1 and h[i + 1] == h[i + 2]:
            total += 1
    for i in range(C - 1):
        if h[i] == h[i + 1]:
            total += 1
        if h[i] == h[i + 1] + 2:
            total += 1
elif P == 7:
    for i in range(C - 2):
        if h[i] == h[i + 1] and h[i + 1] == h[i + 2]:
            total += 1
        if h[i] == h[i + 1] and h[i + 1] == h[i + 2]+1:
            total += 1
    for i in range(C - 1):
        if h[i] == h[i + 1]:
            total += 1
        if h[i] == h[i + 1] - 2:
            total += 1
print(total)
