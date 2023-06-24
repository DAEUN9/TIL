import sys
sys.stdin = open("input.txt", "r")
N = int(input())
num = [0, 1, -1]
curr = 1
answer = ''
target = 1
if N == 0:
    answer = 0
if N < 0:
    minus = True
else:
    minus = False
N = abs(N)
for i in range(1, N):
    curr = i**3
    if curr >= N:
        target = i
        break
while N:
    sup = N%3
    if sup == 2:
        answer = 'T'+answer
        N += 1
    else:
        answer = str(sup)+answer
        N += -sup
    N //= 3

if minus:
    temp = ''
    for a in answer:
        if a == '1':
            temp += 'T'
        elif a == 'T':
            temp += '1'
        else:
            temp += '0'
    answer = temp

print(answer)