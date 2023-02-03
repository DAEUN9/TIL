# 호석이 두 마리 치킨
#
# 그래프 이론
# 브루트포스 알고리즘
# 그래프 탐색
# 너비 우선 탐색
# 플로이드–워셜

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[1000]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    arr[i][i] = 0
hq = []
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            arr[j][k] = min(arr[j][k], arr[j][i]+arr[i][k])
min_val = 1e9
for l in range(1, N):
    for m in range(l+1, N+1):
        val = 0
        for x, y in zip(arr[l][1:], arr[m][1:]):
            val += min(x, y)
        if min_val > val:
            min_val = val
            answer = [l, m]
print(*answer, min_val*2)



"""
실패코드
"""
# arr = [[] for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     arr[a].append(b)
#     arr[b].append(a)
#
# min_total = 1e9
# for i in range(1, N):
#     for j in range(i+1, N+1):
#         hq = []
#         total = 0
#         visited = [0]*(N+1)
#         visited[i], visited[j] = 1, 1
#         for a in arr[i]:
#             heapq.heappush(hq, [1, a])
#         for b in arr[j]:
#             heapq.heappush(hq, [1, b])
#         while hq:
#             curr = heapq.heappop(hq)
#             if visited[curr[1]]:
#                 continue
#             total += curr[0]
#             visited[curr[1]] = 1
#             for c in arr[curr[1]]:
#                 heapq.heappush(hq, [curr[0]+1, c])
#         if total < min_total:
#             min_total = total
#             building = [i, j]
# print(*building, min_total*2)
