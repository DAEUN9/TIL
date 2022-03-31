import sys

sys.stdin = open('input.txt', 'r')

# 회사 개수 N, 경로 개수 M
INF = int(1e9)
N, M = map(int, input().split())
arr = [[INF]*(N+1) for _ in range(N+1)]
for j in range(1, N+1):
    arr[j][j] = 0
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
# 1번 회사부터 시작
# K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간?
X, K =map(int, input().split())
# k는 거쳐가는 노드
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])
answer = arr[1][K] + arr[K][X]
if answer >= INF:
    print(-1)
else:
    print(answer)