import sys
sys.stdin = open("input.txt", "r")

# 주어진 숫자 N, 나눌 수 K
N, K = map(int, input().split())
cnt = 0

while N!=1:
    cnt += N%K
    N -= N%K
    if N == 1:
        break
    cnt += 1
    N //= K
print(cnt)