import sys
sys.stdin = open("input.txt", "r")
H, W = map(int, input().split())
N = int(input())
st_li = [list(map(int, input().split())) for _ in range(N)]
answer = 0
def dfs(idx, cnt, size, a, b):
    global answer
    if cnt >= 2:
        answer = max(answer, size)
        return
    for i in range(idx+1, N):
        x, y = st_li[i]
        if a+x > H:
            if b+y <= W and x <= H:
                dfs(i, cnt+1, size+(x*y), x, y)
        if a+y > H:
            if b+x <= W and y <= H:
                dfs(i, cnt+1, size+(x*y), y, x)
        if b+x > W:
            if a+y <= H and x <= W:
                dfs(i, cnt+1, size+(x*y), y, x)
        if b+y > W:
            if a+x <= H and y <= W:
                dfs(i, cnt+1, size+(x*y), x, y)
        if a+x <= H and b+y <= W:
            dfs(i, cnt+1, size+(x*y), x, y)
        if a+y <= H and b+x <= W:
            dfs(i, cnt+1, size+(x*y), y, x)
for i in range(N):
    x, y = st_li[i]
    if x <= H and y <= W:
        dfs(i, 1, x*y, x, y)
    if y <= H and x <= W:
        dfs(i, 1, x*y, y, x)
print(answer)