import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
input = sys.stdin.readline
# 국가의 수, 비행기 종류 M

def move(i, cnt):
    visited[i] = 1
    for t in tree[i]:
        if not visited[t]:
            cnt = move(t, cnt+1)
    return cnt

for _ in range(T):
    N, M = map(int,input().split())
    tree = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    visited = [0]*(N+1)
    print(move(1, 0))
