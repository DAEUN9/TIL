import sys
sys.stdin = open("input.txt", "r")
board = [list(map(int,input().split())) for _ in range(5)]
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
r, c = map(int, input().split())
flag = False
def solution(x, y, move, cnt):
    global flag
    if move > 3:
        return
    if cnt >= 2:
        flag = True
        return
    for a, b in direction:
        nx = x+a
        ny = y+b
        if 0<=nx<5 and 0<=ny<5:
            if board[nx][ny] == -1:
                continue
            elif board[nx][ny] == 1:
                board[nx][ny] = -1
                solution(nx, ny, move+1, cnt+1)
                board[nx][ny] = 1
            else:
                board[nx][ny] = -1
                solution(nx, ny, move+1, cnt)
                board[nx][ny] = 0
board[r][c] = -1
solution(r, c, 0, 0)
if flag:
    print(1)
else:
    print(0)