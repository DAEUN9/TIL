import sys

sys.stdin = open("input.txt", "r")

D, K = map(int, input().split())
def solution(D, K):
    for j in range(1, K+1):
        for k in range(1, K+1):
            dp = [j, k]
            for i in range(D-2):
                dp.append(dp[-2] + dp[-1])
            if dp[-1] == K:
                return [j, k]
answer = solution(D, K)
for a in answer:
    print(a)