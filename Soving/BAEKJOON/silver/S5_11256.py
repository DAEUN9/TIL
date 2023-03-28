import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    J, N = map(int, input().split())
    boxes = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x : -x[0]*x[1])
    candy = 0
    answer = 0
    for x, y in boxes:
        candy += x*y
        answer += 1
        if candy >= J:
            break
    print(answer)