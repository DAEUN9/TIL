import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
relation = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
answer = []
dq = set()
for _ in range(M):
    a, b = map(int, input().split())
    relation[a][b] = 1
    relation[b][a] = 1
for i in range(1, N+1):
    relation[i][i] = 1
answer_li = []
flag = True
while flag:
    flag = False
    curr = 0
    new = set()
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                if relation[i][j] and not relation[i][k]:
                    new.add((i, k))
    for a, b in new:
        if relation[a][b] == 0:
            relation[a][b], relation[b][a] = 1, 1
            curr += 1
    answer.append(curr)
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if not relation[j][k]:
                flag = True

print(answer)