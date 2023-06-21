import sys
sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
K = min(N, M)
answer = 1
for k in range(1, K+1):
    for n in range(N):
        for m in range(M):
            if n+k >= N or m+k >= M:
                continue
            if arr[n][m] == arr[n+k][m] == arr[n][m+k] == arr[n+k][m+k]:
                answer = max(answer, k+1)
print(answer**2)