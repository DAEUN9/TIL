import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
A, B = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [-1]*(n+1)
visited[A] = 0
dq = deque([A])
while dq:
    curr = dq.popleft()
    for g in graph[curr]:
        if visited[g] < 0:
            visited[g] = visited[curr]+1
            dq.append(g)
print(visited[B])