import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def solution():
    a, b = input().split()
    N, M = map(int, input().split())
    d = dict()
    dq = deque([a])
    visited = dict()
    visited[a] = 0
    for _ in range(M):
        x, y = input().split()
        x_li = d.get(x, [])
        y_li = d.get(y, [])
        d[x] = x_li + [y]
        d[y] = y_li + [x]
    answer = 0
    if a == b:
        return 0
    while dq:
        curr = dq.popleft()
        for i in d[curr]:
            if curr != 1 and visited.get(i):
                continue
            if i == b:
                return visited[curr] + 1
            visited[i] = visited[curr] + 1
            dq.append(i)
    answer = visited.get(b, -1)
    return answer
print(solution())