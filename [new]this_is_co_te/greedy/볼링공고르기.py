import sys
sys.stdin = open("input.txt", "r")

# 볼링공 개수 N, 최대 무게 M
N, M = map(int, input().split())
balls = list(map(int, input().split()))
weight = [0]*(M+1)
for ball in balls:
    weight[ball] += 1

answer = 0
for i in range(1, M):
    N -= weight[i]
    answer += weight[i]*N
print(answer)
