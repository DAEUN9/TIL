# 좋은 수열
# 백트래킹

import sys

sys.stdin = open("input.txt", "r")

N = int(input())
choices = ["1", "2", "3"]
def solution(num):
    global min_num
    if len(num) >= N:
        print(num)
        exit()
    for choice in choices:
        if (check(num+choice)):
            solution(num+choice)


def check(num):
    if len(num) == 1:
        return True
    for i in range(1, len(num)//2 + 1):
        if num[-2 * i : -1 * i] == num[-1 * i :]:
            return False
    return True

solution("")

