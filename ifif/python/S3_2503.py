# 숫자 야구
# 구현, 브루트포스

import sys

sys.stdin = open("input.txt", "r")
T = int(input())
inputList = [list(map(int, input().split())) for _ in range(T)]
answer = 0

def count(num, answer):
    ball = 0
    strike = 0
    for i in range(3):
        if num[i] == answer[i]:
            strike+=1
        elif num[i] in answer:
            ball += 1
    return strike, ball

def check(answer):
    for inp in inputList:
        curr = str(inp[0])
        strike, ball = count(curr, answer)
        if strike != inp[1]:
            break
        if ball != inp[2]:
            break
    else:
        return 1
    return 0


for a in range(1, 10):
    for b in range(1, 10):
        if a==b:
            continue
        for c in range(1, 10):
            if b==c or a==c:
                continue
            answer += check(str(a)+str(b)+str(c))
print(answer)