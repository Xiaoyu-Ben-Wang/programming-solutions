# https://open.kattis.com/problems/bard
num_villagers = int(input())
nights = int(input())

knowledge = {1: {x for x in range(nights)}}
for x in range(2, num_villagers+1):
    knowledge[x] = set()
new_songs = 0
for i in range(nights):
    gathering = {int(x) for x in input().split(' ')[1:]}
    if 1 in gathering:
        new_songs += 1
        for vil in gathering:
            knowledge[vil].add(i)
    else:
        for vil in gathering:
            for vil2 in gathering:
                knowledge[vil] = knowledge[vil2] | knowledge[vil]
for v in sorted(knowledge.keys()):
    if len(knowledge[v]) >= new_songs:
        print(v)
