import sys
sys.stdin = open("input.txt", "r")
C = float(input())
N = int(input())
answer = 1
coins = list(map(int, input().split()))
max_fz = int(min(C//0.99, 2))
curr_fz = 0
end = 0
for i in range(N):
    if i:
        if not coins[i-1]:
            curr_fz -= 1
    while curr_fz <= max_fz:
        if end >= N:
            N -= 1
            break
        if coins[end]:
            end += 1
        else:
            if curr_fz < max_fz:
                end += 1
                curr_fz += 1
            else:
                break
    answer = max(answer, end-i)
print(answer)
print(max(coins))