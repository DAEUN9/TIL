import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')

N, M, V = map(int, sys.stdin.readline().split())
graph = list([0]*(N+1) for n in range(N+1))


dfs_check = [0]*(N+1)
bfs_check = [0]*(N+1)

stack = [V]
def dfs():
    start = stack.pop()
    dfs_check[start] = 1
    print(start, end=' ')
    for n in range(1, N+1):
        if graph[start][n] == 1 and dfs_check[n]==0:
            stack.append(n)
            dfs()



def bfs(start):
    dq = deque([start])
    bfs_check[start]=1
    while dq:
        a = dq.popleft()
        print(a, end=' ')
        for n in range(1, N+1):
            if bfs_check[n]==0 and graph[a][n]==1:
                bfs_check[n]=1
                dq.append(n)



for m in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b], graph[b][a] = 1, 1

dfs()
print()
bfs(V)