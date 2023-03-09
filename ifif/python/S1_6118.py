import sys
from collections import deque
sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())
bridges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    bridges[a].append(b)
    bridges[b].append(a)
dq = deque()
dq.append([1, 0])
visited = [0]*(N+1)
visited[1] = -1
while dq:
    curr, cnt = dq.popleft()
    for b in bridges[curr]:
        if not visited[b]:
            visited[b] = cnt+1
            dq.append([b, cnt+1])

max_num = max(visited)
answer = [0, 0]
for n in range(1, N+1):
    if visited[n] == max_num:
        if answer[0] == 0:
            answer[0] = n
        answer[1] += 1
print(answer[0], max_num, answer[1])