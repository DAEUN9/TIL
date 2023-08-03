import sys
from collections import Counter
sys.stdin = open("input.txt", "r")
T = int(sys.stdin.readline())

num = 0

for i in range(T):
    n, x = list(map(int, sys.stdin.readline().split()))
    v = Counter(list(map(int, sys.stdin.readline().split())))
    if x == 0:
        for c in v.keys():
            num += (v[c] * (v[c] - 1))
    else:
        for c in v.keys():
            num += (v[c] * v[x^c])
    print(num // 2)
    num = 0