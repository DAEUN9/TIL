import sys
sys.stdin = open("input.txt", "r")
'''
N : 앵무새의 수
각 앵무새가 말한 문장 : S(1 <= i <= N)
받아 적은 문장 : L
L이 가능한 문장이면 Possible, 불가능하면 Impossible
'''

N = int(input())
S = []
d = dict()
for _ in range(N):
    words = list(input().split())
    S.append(words)
L = list(input().split())
answer = "Possible"
for l in L:
    for s in S:
        if not s:
            continue
        if s[0] == l:
            s.pop(0)
            break
    else:
        answer = "Impossible"
        break
for s in S:
    if s:
        answer = "Impossible"
print(answer)


