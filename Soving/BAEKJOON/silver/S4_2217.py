# 로프
#
# 그리디

import sys
sys.stdin = open("input.txt", "r")

N = int(input())
ropes = []
for _ in range(N):
    r = int(input())
    ropes.append(r)
ropes.sort(reverse=True)
answer = 0
for i in range(N):
    answer = max(answer, ropes[i]*(i+1))
print(answer)