# https://open.kattis.com/problems/zoo
list = 1
while True:
    num = int(input())
    if (num == 0):
        break

    dict = {}
    for i in range(num):
        animal = input().lower().split(' ')[-1]
        if (animal in dict):
            dict[animal] += 1
        else:
            dict[animal] = 1
    print("List %d:" % list)
    for key in sorted(dict.keys()):
        print("%s | %d" % (key, dict[key]))
    list +=1
