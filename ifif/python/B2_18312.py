# 시각
# 구현, 브루트포스

import sys

sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
cnt = 0
for h in range(N+1):
    if str(K) in str(h).zfill(2):
        cnt += 3600
        continue
    for m in range(60):
        if str(K) in str(m).zfill(2):
            cnt += 60
            continue
        for s in range(60):
            if str(K) in str(s).zfill(2):
                cnt += 1

print(cnt)