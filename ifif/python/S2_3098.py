import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
relation = [[0 for _ in range(N+1)] for i in range(N+1) ]
visited = [0]*(N+1)
dq = set()
for _ in range(M):
    a, b = map(int, input().split())
    relation[a][b], relation[b][a] = 1, 1
answer = 0
answer_li = []
while True:
    answer += 1
    cnt = 0
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    continue
                if relation[i][k] and relation[k][j] and not relation[i][j]:
                    cnt += 1
                    relation[i][j] = relation[j][i] = answer
    flag = True
    for i in range(1, N+1):
        for j in range(1, N+1):
            if relation[i][j] == 0:
                flag=False
                break
    answer_li.append(cnt)
    if flag:
        break
print(answer_li)