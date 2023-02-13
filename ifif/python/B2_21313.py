# 문어
# 그리디, 애드혹

import sys
sys.stdin = open("input.txt", "r")

a = [1, 2]
N = int(input())
answer = []
answer += a *(N//2)
if N%2:
    answer += [3]
print(*answer)