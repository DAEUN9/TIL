import sys

counts = [0]*10001
N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    counts[num] += 1

for i in range(10001):
    if counts[i]:
        for j in range(counts[i]):
            print(i)