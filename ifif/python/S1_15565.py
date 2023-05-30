import sys
sys.stdin = open("input.txt", "r")
N, K = map(int, input().split())
li = list(map(int, input().split()))
d = {1:0, 2:0}
answer = 1e9
end = 0
for i in range(N):
    if i:
        d[li[i-1]] -= 1
    while d[1] < K and i<=end and end < N:
        d[li[end]] += 1
        end += 1
    if d[1] >= K:
        answer = min(answer, end-i)
if answer == 1e9:
    print(-1)
else:
    print(answer)
