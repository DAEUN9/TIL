import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10*1000000)
input = sys.stdin.readline

N, M, R = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort()
visited = [-1]*(N+1)
visited[R] = 0
def dfs(R):
    for node in graph[R]:
        if visited[node] < 0:
            visited[node] = visited[R] + 1
            dfs(node)
dfs(R)
for i in range(1, N+1):
    print(visited[i])