import sys
sys.setrecursionlimit(10**6)

def visit_check(k):
    a = sunyeol[k]
    if visited[a]==0:
        visited[a] = 1
        visit_check(a)
    else:
        return


T = int(input())

for t in range(T):
    N = int(input())

    visited = [0] + [0]*N
    sunyeol = [0] + list(map(int, input().split()))

    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            visit_check(i)
            cnt += 1

    print(cnt)