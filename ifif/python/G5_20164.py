import sys

sys.stdin = open("input.txt","r")
N = input()
b = []


def solution(N, cnt):
    if len(N)==1:
        return cnt + checkOdd(int(N))*2
    if len(N)==2:
        return checkOdd(int(N[0]))*2 + checkOdd(int(N[1]))*2 + cnt
    for i in range(1, len(N)-1):
        for j in range(i+1, len(N)):
                a = int(N[:i])
                b = int(N[i:j])
                c = int(N[j:])
                num = checkOdd(a+b+c)
                print(solution(str(a+b+c), cnt+num))
                return

def checkOdd(num):
    cnt = 0
    while num>1:
        n = num%2
        num %= 2
        if n==0:
           cnt += 1
    return cnt

solution(N, 0)