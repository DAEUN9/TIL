import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
li = [input().split() for t in range(T)]
answer = []
i = 0
for l in li:
    answer.append([int(l[0]), i])
    i += 1
answer.sort()
for i in range(T):
    print(*li[answer[i][1]])