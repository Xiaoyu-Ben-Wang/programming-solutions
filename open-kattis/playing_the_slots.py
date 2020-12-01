# https://open.kattis.com/problems/playingtheslots
num = int(input())
vertices = []
for i in range(num):
    pair = input().split(' ')
    vertices.append((float(pair[0]), float(pair[1])))
answer = []
for i in range(num):
    dists = []
    x1 = vertices[i][0]
    y1 = vertices[i][1]
    x2 = vertices[(i + 1) % num][0]
    y2 = vertices[(i + 1) % num][1]
    for j in range(num):
        x0 = vertices[j][0]
        y0 = vertices[j][1]
        top = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
        bot = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
        d = top / bot
        dists.append(d)
    answer.append(max(dists))
print(min(answer))
