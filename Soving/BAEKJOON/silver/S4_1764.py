import sys
sys.stdin = open('input.txt','r')

# 듣도 못한 수, 보도 못한 수
N, M = map(int, input().split())
d = dict()
for n in range(N):
    curr =input()
    if d.get(curr, 0):
        d[curr] += 1
    else:
        d[curr] = 1
answer = []
for m in range(M):
    curr = input()
    if d.get(curr, 0):
        answer.append(curr)
answer.sort()
print(len(answer))
for a in answer:
    print(a)