import sys
sys.stdin = open("input.txt", "r")
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
answer = 0
def dfs(x, y, cnt, move):
    global answer
    if move > 3:
        return
    if cnt >= 2:
        answer = 1
        return
    for a, b in direction:
        nx = a+x
        ny = b+y
        if 0<=nx<5 and 0<=ny<5 and board[nx][ny] > -1:
            if board[nx][ny] == 1:
                board[nx][ny] = -1
                dfs(nx, ny, cnt+1, move+1)
                board[nx][ny] = 1
            elif board[nx][ny] == 0:
                board[nx][ny] = -1
                dfs(nx, ny, cnt, move+1)
                board[nx][ny] = 0
board[r][c] = -1
dfs(r, c, 0, 0)
print(answer)