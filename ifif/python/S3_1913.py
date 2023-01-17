import sys


sys.stdin = open("input.txt", "r")

N = int(input())
target = int(input())

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
arr = [[0 for _ in range(N)] for _ in range(N)]
arr[0][0] = N**2
x, y, idx = 0, 0, 0
n = N**2-1

def snail(x, y, n, N, idx):
    d = direction[idx]
    dx = x + d[0]
    dy = y + d[1]
    if 0<=dx<N and 0<=dy<N and arr[dx][dy]==0:
        x, y = dx, dy
        arr[x][y] = n
        n -= 1
    else:
        idx += 1
    return x, y, n, idx

while n>=1:
    idx = idx%4
    x, y, n, idx = snail(x, y, n, N, idx)
target_x = 0
target_y = 0
for row in range(N):
    if target in arr[row]:
        target_x = row
        target_y = arr[row].index(target)
    print(*arr[row])
print(target_x+1, target_y+1)

