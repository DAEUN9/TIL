import sys
sys.stdin = open("input.txt", "r")

paper = [[0]*100 for _ in range(100)]
N = int(input())
for _ in range(N):
    x, y = map(int,input().split())
    for a in range(10):
        for b in range(10):
            nx, ny = a+x, b+y
            paper[nx][ny] = 1

cnt = 0
for r in range(100):
    for c in range(100):
        if paper[r][c]:
            cnt += 1

print(cnt)