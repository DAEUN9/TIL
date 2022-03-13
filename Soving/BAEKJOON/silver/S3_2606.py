import sys
from collections import deque

sys.stdin = open('input.txt','r')

com_cnt = int(sys.stdin.readline())
line_cnt = int(sys.stdin.readline())
lines = list(list(map(int, sys.stdin.readline().split())) for _ in range(line_cnt))
check = list([0]*(com_cnt+1) for _ in range(com_cnt+1))


for l in lines:
    check[l[0]][l[1]] = 1
    check[l[1]][l[0]] = 1
answer = [0]*(com_cnt+1)

def bfs():
    dq = deque([1])
    while dq:
        curr = dq.popleft()
        answer[curr] = 1
        idx = 0
        for i in check[curr]:
            if i and answer[idx]==0:
                dq.append(idx)
            idx += 1

bfs()
print(answer.count(1)-1)