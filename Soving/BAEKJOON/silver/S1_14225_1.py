import sys
import itertools

sys.stdin = open('input.txt', 'r')
N = int(input())
li = list(map(int, input().split()))
total = [0]*(sum(li)+1)
for i in range(1, N+1):
    for j in itertools.combinations(li, i):
        total[sum(j)] = 1
answer = sum(li)+1
for i in range(1, sum(li)+1):
    if total[i]:
        continue
    answer = i
    break
print(answer)