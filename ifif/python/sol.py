import sys
from collections import deque
sys.stdin = open("input.txt", "r")
def solution():
    a, b = input().split()
    N, M = map(int, input().split())
    d = dict()
    visited = dict()
    for _ in range(M):
        x, y = input().split()
        temp1 = d.get(x, [])
        temp2 = d.get(y, [])
        d[x], d[y] = temp1 + [y], temp2 + [x]
    dq = deque([a])
    visited[a] = 1
    if a == b:
        return 0
    while dq:
        curr = dq.popleft()
        for next in d[curr]:
            if not visited.get(next):
                visited[next] = visited[curr] + 1
                if next == b:
                    return visited[next]-1
                dq.append(next)
    return -1
print(solution())