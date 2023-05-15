import sys
sys.stdin = open("input.txt", "r")
N = int(input())
d = dict()
for _ in range(N-1):
    A, B = input().split()
    temp = d.get(B, [])
    temp.append(A)
    d[B] = temp

a, b = input().split()
