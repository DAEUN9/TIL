import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

li = [tuple(map(int, input().split())) for t in range(N)]
li1 = []
for l in li:
    b,a = l[0], l[1]
    li1.append((a, b))
li1.sort()
gijun = li1[0]
answer = 1
for l in li1[1:]:
    if l[1]>=gijun[0]:
        answer += 1
        gijun = l
print(answer)
