from collections import deque

def solution(n, edge):
    dist = [[] for _ in range(n+1)]
    visited = [-1]*(n+1)
    visited[1] = 0
    for a, b in edge:
        dist[a].append(b)
        dist[b].append(a)
    dq = deque([1])
    while dq:
        curr = dq.popleft()
        for d in dist[curr]:
            if visited[d] > -1:
                continue
            visited[d] = visited[curr] + 1
            dq.append(d)
    
    max_num = max(visited)
    
    return visited.count(max_num)