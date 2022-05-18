import sys
sys.stdin = open('input.txt', 'r')

# 세로, 가로
H, W = map(int, input().split())

li = list(map(int, input().split()))
edge = 0
max_num = 0
total = 0
for i in range(1, W):
    if li[i] >= li[edge]:
        for j in range(edge+1, i):
            total += li[edge] - li[j]
        edge = i
        max_num = 0
    else:
        if li[i] > max_num:
            max_num = i
print(total)