import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
answer = 0
# direction = [[0, 0], [0, -1], [-1, -1], [-1, 0]]
arr1 = [[0] * (M+1) for _ in range(N+1)]
def solution(num):
    global answer
    if num >= N*M:
        answer += 1
        return
    x = num // M+1
    y = num % M+1
    solution(num+1)
    if arr1[x-1][y] == 0 or arr1[x][y-1]==0 or arr1[x-1][y-1]==0:
        arr1[x][y] = 1
        solution(num+1)
        arr1[x][y] = 0

solution(0)
print(answer)