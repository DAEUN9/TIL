import sys
sys.setrecursionlimit(10**7)

sys.stdin = open('input.txt','r')

input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
cnt = 0
def DFS(r,c,n):
    global cnt
    if r<0 or c<0 or r>=M or c>=N:
        return 0
    answer = 0
    if n>arr[r][c]:
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr = dr + r
            nc = dc + c
            answer += DFS(nr, nc, )
DFS(0, 0, 99999)
print(cnt)