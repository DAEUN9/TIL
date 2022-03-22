# 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

import sys
from collections import deque
sys.setrecursionlimit(10**9)

sys.stdin = open('input.txt', 'r')

# 노드의 개수
N = int(sys.stdin.readline())

tree = list([] for _ in range(N+1))
visit = [0] * (N+1)

for n in range(1, N):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def BFS(s):
    dq = deque([s])
    visit[s] = 1
    while dq:
        curr = dq.pop()
        for i in tree[curr]:
            if not visit[i]:
                visit[i] = curr
                dq.append(i)

BFS(1)
for i in range(2, N+1):
    print(visit[i])