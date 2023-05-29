def solution(n, s, a, b, fares):
    INF = 1e9
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    graph[i][j] = 0
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    answer = graph[s][a] + graph[s][b]
    for l in range(1, n + 1):
        answer = min(answer, graph[s][l] + graph[l][a] + graph[l][b])
    return answer