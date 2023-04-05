import sys
sys.stdin = open("input.txt", "r")
N = int(input())
r_numbers = [1, 5, 10, 50]
cnt = dict()
def dfs(n, curr, idx):
    if n == N:
        cnt[curr] = 1
        return
    if idx == 4:
        return
    for i in range(N+1):
        if n+i <= N:
            dfs(n+i, curr+r_numbers[idx]*i, idx+1)
dfs(0, 0, 0)
print(len(cnt))