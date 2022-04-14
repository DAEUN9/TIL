import sys
sys.stdin = open('input.txt', 'r')


# 정점 개수 V, 간선 개수 E
# V, E = map(int, input().split())
# INF = int(1e9)
# graph = [[INF]*(V+1) for _ in range(V+1)]
# for i in range(1, V+1):
#     graph[i][i] = 0
#
# for _ in range(E):
#     # 정점, 정점, 가중치
#     A, B, C = map(int, input().split())
#     graph[A][B] = C
#     graph[B][A] = C
#
# for k in range(1, V+1):
#     for a in range(1, V+1):
#         for b in range(1, V+1):
#             graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
def find_parent(x):
    while parent[x] != x:
        x = parent[x]
    return parent[x]

V, E = map(int, input().split())
parent = [0]*(V+1)
for i in range(1, V+1):
    parent[i] = i
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
total = 0
for edge in edges:
    c, a, b = edge
    x = find_parent(a)
    y = find_parent(b)
    if x != y:
        if x <y:
            parent[y] = x
        else:
            parent[x] = y
        total += c

print(total)