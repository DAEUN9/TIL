import sys
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline
N = int(input())
works = []
for _ in range(N):
    works.append(list(map(int, input().split())))
works.sort(key=lambda x : -x[1])

curr = works[0][1]
for t, s in works:
    if curr > s:
        curr = s
    curr -= t
if curr >= 0:
    print(curr)
else:
    print(-1)