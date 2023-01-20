import sys


sys.stdin = open("input.txt", "r")

N, M, R = map(int, input().split())
arr = list( list(map(int, sys.stdin.readline().split())) for _ in range(N))
direction = [(1,0), (0,1), (-1,0), (0,-1)]

for _ in range(R):
    for r in range(min(N,M)//2):
        idx = 0
        x, y = r, r
        curr = arr[r][r]
        for d in direction:
            while True:
                dx = x+d[0]
                dy = y+d[1]
                if(r<=dx<N-r) and (r<=dy<M-r):
                    x, y = dx, dy
                    arr[x][y], curr = curr, arr[x][y]
                else:
                    break
for ar in arr:
    print(*ar)