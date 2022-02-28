import sys

N= int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for n in range(N)]

arr.sort()

for a in arr:
    print(*a)