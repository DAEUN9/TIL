def solution(n, results):
    answer = 0
    graph = [[0]*(n+1) for _ in range(n+1)]
    for A, B in results:
        graph[A][B] = 1
        graph[B][A] = -1
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    continue
                if graph[i][k]== 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                continue
            if not graph[i][j]:
                break
        else:
            answer += 1
    return answer