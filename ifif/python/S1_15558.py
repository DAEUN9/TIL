import sys
from collections import deque
sys.stdin = open("input.txt", "r")
N, k = map(int, input().split())
lines = [list(map(int, list(input()))) for _ in range(2)]
dq = deque()
dq.append([0, 0, 1])
visited = [[0]*N for _ in range(2)]
visited[0][0] = 1
while dq:
    a, b, c = dq.popleft()
    # 라인 번호, 칸, 시간
    if b >= N or b+k >= N:
        print(1)
        break
    if not visited[a][b+1] and lines[a][b+1]:
        visited[a][b+1] = 1
        dq.append([a, b+1, c+1])
    if c < b and lines[a][b-1] and not visited[a][b-1]:
        visited[a][b-1] = 1
        dq.append([a, b-1, c+1])
    if lines[(a+1)%2][b+k] and not visited[(a+1)%2][b+k]:
        visited[(a+1)%2][b+k] = 1
        dq.append([(a+1)%2, b+k, c+1])
else:
    print(0)