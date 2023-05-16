import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N+1)]
depth = [0] * (N+1)
visited = [0] * (N+1)
cnt = 0
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(curr):
    for t in tree[curr]:
        if not visited[t]:
            depth[t] = depth[curr] + 1
            visited[t] = 1
            dfs(t)
visited[1] = 1
dfs(1)
for i in range(2,N+1):
    if len(tree[i]) == 1:
        cnt += depth[i]

if cnt%2:
    print("Yes")
else:
    print("No")