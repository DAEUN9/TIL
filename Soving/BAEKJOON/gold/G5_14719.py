import sys
sys.stdin = open('input.txt', 'r')

# 세로, 가로
H, W = map(int, input().split())

li = list(map(int, input().split()))
total = 0

for i in range(1, W-1):
    left = max(li[:i])
    right = max(li[i+1:])
    m = min(left, right)
    if m> li[i]:
        total += m-li[i]
print(total)