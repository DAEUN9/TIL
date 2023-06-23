import sys
sys.stdin = open("input.txt", "r")
N = int(input())
num = [0, 1, -1]
curr = 1
answer = 0
target = [0, 0]
if N < 0:
    minus = True
else:
    minus = False
N = abs(N)
for i in range(1, N):
    curr *= i
    if curr >= N:
        target = [i-1, i]
        break
def make_three(n, string, idx):
    global N, answer
    if N == n:
        answer = string
        return
    if target[1] <= idx:
        return
    for u in num:
        if u == -1:
            ss = 'T'
        else:
            ss = str(u)
        make_three(n + u*3**idx, ss + string, idx+1)
make_three(0, '', 0)
if minus:
    answer = answer[::-1]
print(answer)