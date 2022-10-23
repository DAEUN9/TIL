# 그래프
# https://school.programmers.co.kr/learn/courses/30/lessons/49189?language=python3

def solution(n, edge):
    INF = 1e9
    dist = [[INF]*(n+1) for _ in range(n+1)]
    for c in range(1, n+1):
        dist[c][c] = 0
    for a, b in edge:
        dist[a][b] = 1
        dist[b][a] = 1
    for k in range(1, n+1):
        for i in range(1, n+1):
             for j in range(1, n+1):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    print(dist)
    max_num = max(dist[1][1:])
    answer = dist[1].count(max_num)
    return answer