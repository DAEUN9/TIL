import sys
sys.stdin = open('input.txt','r')

from collections import deque

def BFS(n, k):
    q = deque()
    q.append((0, n))
    while q:
        cnt, num = q.popleft()
        if num == k:
            return cnt
        if 0<=num+1<=100000 and not visited[num+1]:
            visited[num+1] = True
            q.append((cnt+1, num+1))
        if 0<=num-1<=100000 and not visited[num-1]:
            visited[num-1] = True
            q.append((cnt+1, num-1))
        if 0<=num*2<=100000 and not visited[num*2]:
            visited[num*2] = True
            q.append((cnt+1, num*2))
N, K = map(int, input().split())
visited = [False]*(100001)

answer = BFS(N, K)
print(answer)