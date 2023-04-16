import sys
import math
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N, L = map(int, input().split())
boards = []
for _ in range(N):
    x, y = map(int, input().split())
    boards.append([x, y])

boards.sort()
curr = 0
cnt = 0
for x, y in boards:
    if x > curr:
        curr = x
    temp_cut = math.ceil((y-curr)/L)
    cnt += temp_cut
    curr += temp_cut*L


print(cnt)