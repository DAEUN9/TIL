import sys

sys.stdin = open('input.txt', 'r')

# 행 개수 N, 열 개수 M
N, M = map(int, input().split())
arr = list(list(map(int, input().split())) for i in range(N))

target = 0
for a in arr:
    target = max(min(a), target)
print(target)