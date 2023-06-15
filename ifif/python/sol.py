import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
figure = list(list(map(int, input().split())) for _ in range(N))
answer = N*M
for i in range(N):
    for j in range(M):
        if j == 0 :
            answer += figure[i][j]
            continue
        answer += max(0, figure[i][j] - figure[i][j-1])

for j in range(M):
    for i in range(N):
        if i == 0 :
            answer += figure[i][j]
            continue
        answer += max(0, figure[i][j] - figure[i-1][j])
print(answer*2)