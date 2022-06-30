import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline
# 행, 열, 초
R, C, N = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]


# 폭탄 놓기
if N%2==0:
    for r in range(R):
        print('O'*C)
# 원래 터짐
elif N%2 and N%3==0:
    bomb = [['O' for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if arr[r][c]=='O':
                bomb[r][c] = '.'
                for x, y in [(1, 0), (-1, 0), (0,1), (0,-1)]:
                    nr = x + r
                    nc = y + c
                    if 0<=nr<R and 0<=nc<C:
                        bomb[nr][nc]='.'
    for b in bomb:
        print(''.join(b))
# 원래대로
else:
    for a in arr:
        print(''.join(a))