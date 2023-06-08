import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
li = list(map(int, input().split()))
d = {1:0, 2:0}
end = 0
answer = 1e9
for i in range(N):
    if i:
        d[li[i-1]] -= 1
    while end<N:
        if d[1] >= K:
            break
        d[li[end]] += 1
        end += 1


    if d[1] >= K:
        answer = min(answer, end - i)

if answer == 1e9:
    print(-1)
else:
    print(answer)