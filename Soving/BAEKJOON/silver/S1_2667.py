# 단지번호붙이기
import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
tracks = list(list(map(int, list(sys.stdin.readline().rstrip()))) for n in range(N))
arr = list([0]*N for n in range(N))

stack = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs():
    cnt = 1
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            while 0<=nr<N and 0<=nc<N and tracks[nr][nc] and arr[nr][nc]==0:
                cnt += 1
                stack.append([nr, nc])
                arr[nr][nc] = 1
                nr = nr + dr[i]
                nc = nc + dc[i]

    return cnt

answer = []
cnt = 0
for i in range(N):
    for j in range(N):
        if tracks[i][j] == 1 and arr[i][j]==0:
            arr[i][j]=1
            stack.append([i, j])
            answer.append(dfs())
            cnt += 1
print(cnt)
answer.sort()
for a in answer:
    print(a)
