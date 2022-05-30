import sys
sys.setrecursionlimit(10**7)

sys.stdin = open('input.txt','r')

input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[-1] * N for _ in range(M)]
def DFS(r,c):
    if r == M -1 and c == N-1:
        return 1
    if visited[r][c] != -1:
        return visited[r][c]

    visited[r][c] = 0
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr = dr + r
        nc = dc + c
        if 0<=nr<M and 0<=nc<N:
            if arr[r][c] > arr[nr][nc]:
                visited[r][c] += DFS(nr, nc)

    return visited[r][c]
print(DFS(0, 0))