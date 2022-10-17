import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    sx, sy, ex, ey = map(int, input().split())
    # 행성의 개수
    n = int(input())
    answer = 0
    for _ in range(n):
        x, y, r = map(int, input().split())
        if ((sx-x)**2 + (sy-y)**2) < r**2 and ((ex-x)**2 + (ey-y)**2) < r**2:
            continue
        elif ((sx-x)**2 + (sy-y)**2) < r**2:
            answer += 1
        elif ((ex-x)**2 + (ey-y)**2) < r**2:
            answer += 1
    print(answer)