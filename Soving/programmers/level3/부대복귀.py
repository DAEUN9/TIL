# 시간초과
def solution(n, roads, sources, destination):
    answer = []
    distances = [1e9 for _ in range(n+1)]
    visited = [False] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for a, b in roads:
        graph[a].append([b, 1])
        graph[b].append([a, 1])
    def get_smallest_node():
        min_val = 1e9
        index = 0
        for i in range(1, n+1):
            if not visited[i] and distances[i] < min_val:
                min_val = distances[i]
                index = i
        return index
    
    def dijkstra(start):
        distances[start] = 0
        visited[start] = True
        for i in graph[start]:
            distances[i[0]] = i[1]
        for _ in range(n-1):
            now = get_smallest_node()
            visited[now] = True
            for next in graph[now]:
                cost = distances[now] + next[1]
                if cost < distances[next[0]]:
                    distances[next[0]] =cost
    dijkstra(destination)
    for source in sources:
        if distances[source] == 1e9:
            answer.append(-1)
            continue
        answer.append(distances[source])
    
    return answer