import sys

sys.stdin = open('input.txt', 'r')

T = 10
# N극 아래로 떨어짐 1
# S극 위로 올라감 2
for t in range(1, T+1):
    N= int(input())
    arr = [list(map(int, (input().split()))) for i in range(N)]

    deadlock = 0

    for i in range(N):
        prev = 0
        for j in range(N):
            if arr[j][i] !=0 and prev==0:
                prev = arr[j][i]
            elif arr[j][i] != 0 and prev != arr[j][i]:
                prev = arr[j][i]
                if prev == 2:
                    deadlock += 1
    print(f'#{t}', deadlock)