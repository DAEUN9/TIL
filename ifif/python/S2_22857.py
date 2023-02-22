# 가장 긴 짝수 연속한 부분 수열 (small)
#
# 다이나믹 프로그래밍
# 두 포인터

import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
S = list(map(int, input().split()))
cnt = 0
start = 0
end = 0
answer = 0
while start<N and end<N and start<=end:
    if cnt<=K:
        answer = max(answer, end-start-cnt)
        if start ==0 and S[start]%2==0:
            answer = max(answer, end-start-cnt+1)
        end += 1
        if end<N and S[end]%2:
            cnt += 1
    elif cnt>K:
        start += 1
        if S[start]%2:
            cnt -= 1
print(answer)


