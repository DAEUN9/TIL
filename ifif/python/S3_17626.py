# 브루트포스, dp
# Four Squares

import math
import sys

sys.stdin = open("input.txt", "r")
N = int(input())
def solution(n):
    if math.sqrt(n).is_integer():
        return 1

    squareList = [i**2 for i in range(1, int(math.sqrt(n))+1)]

    for square in squareList:
        if n-square in squareList:
            return 2

    for a in squareList:
        for b in squareList:
            if n-a-b in squareList:
                return 3

    return 4

print(solution(N))