# 근손실
# 백트래킹

import sys

sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
kitList = list(map(int, input().split()))
answer = 0
def solution(visited, weight, K):
    global answer
    if weight < 500:
        return
    if sum(visited) == len(visited):
        answer += 1
        return
    for i in range(len(kitList)):
        if visited[i]:
            continue
        visited[i] = 1
        solution(visited, weight-K+kitList[i], K)
        visited[i] = 0
solution([0]*N, 500, K)
print(answer)