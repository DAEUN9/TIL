import sys
sys.stdin = open("input.txt", "r")
N = int(input())
route = list(map(int, input().split()))
size = 1
depth = [0] * N
depth[route[0]] = -1
tree = dict()
tree[route[0]] = 1
for i in range(1, N):
    if not tree.get(route[i]):
        depth[route[i]] = route[i-1]
        tree[route[i]] = 1
        size += 1
print(size)
for j in range(size):
    print(depth[j], end=" ")

