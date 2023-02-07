# 브루트포스 알고리즘
# 백트래킹

# 연산자 끼워넣기(2)

import sys

sys.stdin = open("input.txt", "r")

N = int(input())
li = list(map(int, input().split()))
cal = list(map(int, input().split()))
answer = [-1e9, 1e9]

def solution(idx, result, calculators):
    if idx==len(li):
        answer[0] = max(answer[0], result)
        answer[1] = min(answer[1], result)
        return
    if calculators[0]:
        calculators[0] -= 1
        solution(idx+1, result+li[idx], calculators)
        calculators[0] += 1
    if calculators[1]:
        calculators[1] -= 1
        solution(idx+1, result-li[idx], calculators)
        calculators[1] += 1
    if calculators[2]:
        calculators[2] -= 1
        solution(idx+1, result*li[idx], calculators)
        calculators[2] += 1
    if calculators[3]:
        calculators[3] -= 1
        temp = result//li[idx]
        if temp>=0:
            solution(idx+1, result//li[idx], calculators)
        else:
            solution(idx+1, abs(result)//abs(li[idx])*-1, calculators)
        calculators[3] += 1

solution(1, li[0], cal)
print(answer[0])
print(answer[1])