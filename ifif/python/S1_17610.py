import sys
sys.stdin = open("input.txt", "r")
K = int(input())
chus = list(map(int, input().split()))
answer = [0]*(sum(chus)+1)
def dfs(curr, idx):
    global K
    if curr>=0 and not answer[curr]:
        answer[curr] = 1
    if idx == K:
        return
    dfs(curr+chus[idx], idx+1)
    dfs(curr-chus[idx], idx+1)
    dfs(curr, idx+1)
dfs(0, 0)
print(answer.count(0))