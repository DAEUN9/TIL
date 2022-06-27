import sys

sys.stdin = open('input.txt', 'r')

# 회원의 수
N = int(input())
INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0
while True:
    s, e = map(int, input().split())
    if s == -1 and e == -1:
        break
    graph[s][e] = 1
    graph[e][s] = 1

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

score = [[] for _ in range(N+1)]
for i in range(1, N+1):
    idx = max(graph[i][1:])
    score[idx].append(i)

for j in range(1, N+1):
    if score[j]:
        print(j, len(score[j]))
        print(*score[j])
        break