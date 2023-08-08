import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
N, M = map(int, input().split())
d = dict()
for _ in range(N):
    d[input().strip()] = 1
for _ in range(M):
    keywords = input().strip().split(",")
    for keyword in keywords:
        if d.get(keyword):
            del d[keyword]
    print(len(d))