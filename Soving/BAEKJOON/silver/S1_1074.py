import sys
sys.stdin = open('input.txt','r')

N, r, c = map(int, input().split())
arr=[[0]*N**2 for _ in range(N**2)]
print(arr)
cnt = 0
for x, y in [(0, 0), (0, 1), (-1, 0), (-1, 1)]:
    nr = r + x
    nc = c + y
    arr[nr][nc] = cnt
def Z(n):
    n = n//2
