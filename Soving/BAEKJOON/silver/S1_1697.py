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

d = [-1, 1]
def BFS(n, k):
    q = deque()
    q.append((0, n))
    while q:
        cnt, num = q.popleft()
        if num == k:
            return cnt
        for i in range(3):
            if i==2:
                move = num*2
            else:
                move = num + d[i]
            if 0<=move<=100000 and not visited[move]:
                visited[move] = True
                q.append((cnt+1, move))

N, K = map(int, input().split())
visited = [False]*(100001)

answer = BFS(N, K)
print(answer)