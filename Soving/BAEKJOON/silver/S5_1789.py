# 수들의 합
# https://www.acmicpc.net/problem/1789

S = int(input())

total = 0
cnt = 0
while total != S:
    cnt += 1
    total += cnt
    if total > S:
        cnt -= 1
        break

print(cnt)