# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141J8KAIcCFAYD
# 사칙연산

import sys
sys.stdin = open('input.txt', 'r')

T = 10
asmd = '+*-/'
for t in range(1, T+1):
    N = int(input())
    linked = dict()
    value = dict()
    for n in range(1, N+1):
        li = input().split()
        if len(li) >=3:
            linked[li[0]] = [li[2], li[3]]
        else:
            linked[li[0]] = 0
        value[li[0]] = li[1]

    def sunhwe(v):
        if linked[v]:
            a = sunhwe(linked[v][0])
            b = sunhwe(linked[v][1])
            return yeonsan(a, b, value[v])
        else:
            return int(value[v])


    def yeonsan(x, y, giho):
        if giho=='+':
            return x+y
        elif giho=='*':
            return x*y
        elif giho=='-':
            return x-y
        elif giho=='/':
            return x/y

    print(f'#{t}', int(sunhwe('1')))