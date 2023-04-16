import sys
sys.stdin = open("input.txt", "r")
N, L = map(int, input().split())
boards = []
for _ in range(N):
    x, y = map(int, input().split())
    boards.append([x, y])

boards.sort()
for x, y in boards:
    