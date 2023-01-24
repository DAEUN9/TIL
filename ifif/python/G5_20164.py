import sys

sys.stdin = open("input.txt","r")
N = input()
answer = [1e9, 0]


def solution(N, cnt):
    if len(N)==1:
        answer[0] = min(cnt, answer[0])
        answer[1] = max(cnt, answer[1])
        return
    if len(N)==2:
        N = str(int(N[0])+int(N[1]))
        return solution(N, cnt+checkOdd(N))
    for i in range(1, len(N)-1):
        for j in range(i+1, len(N)):
                a = int(N[:i])
                b = int(N[i:j])
                c = int(N[j:])
                num = checkOdd(a+b+c)
                solution(str(a+b+c), cnt+num)

def checkOdd(num):
    cnt = 0
    for n in str(num):
        if n in "13579":
            cnt+=1
    return cnt

solution(N, 0)
origin = checkOdd(N)
answer[0] += origin
answer[1] += origin
print(*answer)