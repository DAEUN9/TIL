import sys
sys.stdin = open("input.txt", "r")
def solution(idx, S, curr, cnt, k):
    if cnt == k:
        c = d.get(curr, 0)
        d[curr] = c+1
        return
    for i in range(idx+1, len(S)):
        solution(i, S, curr+S[i], cnt+1, k)

X = input()
Y = input()
Z = input()
k = int(input())
d = dict()

solution(-1, X, "", 0, k)
solution(-1, Y, "", 0, k)
solution(-1, Z, "", 0, k)
flag = True
keys = sorted(d.keys())
for key in keys:
    if d[key] >= 2:
        flag = False
        print(key)
if flag:
    print(-1)