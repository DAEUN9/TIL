# 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389

import sys
sys.stdin = open('input.txt', 'r')

# 유저 수 N, 친구 관계 수 M
N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
answer = 1
min_val = INF*N
for an in range(1, N+1):
    a = sum(graph[an])
    if min_val > a:
        min_val = a
        answer = an
print(answer)