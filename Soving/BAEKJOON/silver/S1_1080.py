# 행렬
#
# 그리디 알고리즘

import sys
sys.stdin = open("input_dt.txt", "r")

N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]

def reverse(r, c):
    # 3*3 행렬을 모두 뒤집기
    for x in range(r, r+3):
        for y in range(c, c+3):
            A[x][y] = (A[x][y]+1)%2
if A==B:
    print(0)
elif N<3 or M<3:
    print(-1)
else:
    cnt = 0
    # 3*3행렬 범위 초과하지 않는 범위
    for r in range(N-2):
        for c in range(M-2):
            # 첫 원소만 비교
            # r, c 다음 칸들은 순서가 되었을 때 뒤집어 주면 됨
            if A[r][c] != B[r][c]:
                cnt += 1
                reverse(r, c)
    if cnt and A==B:
        print(cnt)
    else:
        print(-1)

