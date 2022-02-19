import sys

N= int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for n in range(N)]

for n in range(N-1):
    for i in range(n+1, N):
        if arr[n][0] > arr[i][0]:
            arr[n], arr[i] = arr[i], arr[n]
        elif arr[n][0] == arr[i][0]:
            if arr[n][1] > arr[i][1]:
                arr[n], arr[i] = arr[i], arr[n]
for a in arr:
    print(*a)
