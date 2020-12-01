# https://open.kattis.com/problems/tajna
message = input()
length = len(message)
# get matrix
R = 1
C = length
for i in range(1, length):
    if ((length // i) * i == length) and i <= length//i:
        R = i
        C = length // i

matrix = [['' for _ in range(C)] for i in range(R)]

counter = 0
for column in range(C):
    for row in range(R):
        matrix[row][column] = message[counter]
        counter += 1
answer = ''
for x in matrix:
    for y in x:
        answer += y
print(answer)
