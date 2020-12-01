# https://open.kattis.com/problems/snappereasy
cases = int(input())
answers = []
for _ in range(cases):
    pair = input().split(' ')
    count = int(pair[0])
    snaps = int(pair[1])
    # Powered, On
    array = [[False, False] for x in range(count)]
    array[0] = [True,False]

    for x in range(snaps):
        # snap turns them on/off
        for i in range(count):
            if array[i][0] == True:
                if array[i][1] == True:
                    array[i][1] = False
                else:
                    array[i][1] = True
        for i in range(count - 1):
            if array[i][0] == True and array[i][1] == True:
                array[i + 1][0] = True
            else:
                array[i+1][0] = False
    answers.append(array[-1][0] and array[-1][1])
for i in range(cases):
    if answers[i]:
        print("Case #%d: ON" % (i+1))
    else:
        print("Case #%d: OFF" %(i+1))
