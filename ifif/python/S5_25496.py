import sys
sys.stdin = open("input.txt", "r")
P, N = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
cnt =0
for a in A:
    if P >= 200:
        break
    P += a
    cnt += 1

print(cnt)