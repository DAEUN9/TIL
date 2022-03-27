# N과 M(4)
# https://www.acmicpc.net/problem/15652

def suyeol(n, m, l):
    if len(l) == m:
        print(*l)
        return
    for i in range(1, N+1):
        if l and l[-1]>i:
            continue
        suyeol(n+1, m, l+[i])

# 1~N까지, 수열길이 M
N, M = map(int, input().split())

suyeol(N, M, [])

