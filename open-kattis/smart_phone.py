# https://open.kattis.com/problems/smartphone
cases = int(input())
answers = []
for _ in range(cases):
    goal = input()
    typed = input()
    sugs = [input(), input(), input()]

    options = []
    # using typed
    keypresses = len(goal)
    deletes = 0
    if (len(typed) > len(goal)):
        for i in range(len(goal)):
            if goal[i] == typed[i]:
                keypresses -= 1
            else:
                deletes += len(goal) - i
                break
        deletes += len(typed) - len(goal)
        options.append(deletes + keypresses)
    else:
        for i in range(len(typed)):
            if goal[i] == typed[i]:
                keypresses -= 1
            else:
                deletes += len(typed) - i
                break
        options.append(deletes + keypresses)

    for x in range(3):
        keypresses = len(goal)
        deletes = 0
        if (len(sugs[x]) > len(goal)):
            for i in range(len(goal)):
                if goal[i] == sugs[x][i]:
                    keypresses -= 1
                else:
                    deletes += len(goal) - i
                    break
            deletes += len(sugs[x]) - len(goal)
            options.append(deletes + keypresses+1)
        else:
            for i in range(len(sugs[x])):
                if goal[i] == sugs[x][i]:
                    keypresses -= 1
                else:
                    deletes += len(sugs[x]) - i
                    break
            options.append(deletes + keypresses+1)
    answers.append(min(options))


for i in range(len(answers)):
    print(answers[i])
