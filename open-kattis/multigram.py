# https://open.kattis.com/problems/multigram
cases = int(input())
answers = []
for _ in range(cases):
    days, months = input().split(' ')
    days = int(days)
    months = int(months)
    days_in_month = input().split(' ')

    fridays = set()
    for i in range(days//7):
        fridays.add(i * 7 + 5)
    if (days // 7 * 7 + 5 <= (days - 1)):
        fridays.add(days // 7 * 7 + 5)

    thirteenths = set()
    for i in range(months):
        if int(days_in_month[i]) >= 13:
            total = 0
            for j in range(i):
                total += int(days_in_month[j])
            thirteenths.add(12 + total)

    answers.append(len(fridays & thirteenths))
for i in range(cases):
    print(answers[i])
