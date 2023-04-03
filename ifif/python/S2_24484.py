import sys
sys.stdin = open("input.txt", "r")
N, M, R = map(int, input().split())
lines = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    lines[u][v], lines[v][u] = 1, 1
visited = [0]*(N+1)
visited[R] = 1
answer = 0
idx = 1
def dfs(R):
    global answer, idx
    for i in range(N, 0, -1):
        if lines[R][i] and not visited[i]:
            visited[i] = 1
            answer += idx*R
            idx += 1
            dfs(i)
dfs(R)
print(answer)

