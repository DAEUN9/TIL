import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())
T = [[] for _ in range(n)]
visited = [0]*n
dq = deque()
dq.append([0,0])
visited[0] = 1
answer = 0

for _ in range(n-1):
    p, c = map(int, input().split())
    T[p].append(c)
cnt_li = list(map(int, input().split()))
if cnt_li[0]:
    answer += 1

while dq:
    curr, distance = dq.popleft()
    if distance >= k:
        continue
    for t in T[curr]:
        if not visited[t]:
            visited[t] = 1
            dq.append([t, distance+1])
            if cnt_li[t]:
                answer += 1
print(answer)