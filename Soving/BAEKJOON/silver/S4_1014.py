import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
P = []
for n in range(N):
    idx = B.index(A[n])
    P.append(idx)
    B[idx] -= 1
print(*P)