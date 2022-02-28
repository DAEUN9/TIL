import sys

N= int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for n in range(N)]

for a in arr:
    a[0], a[1] = a[1], a[0]
arr.sort()

for a in arr:
    a[0], a[1] = a[1], a[0]
    print(*a)