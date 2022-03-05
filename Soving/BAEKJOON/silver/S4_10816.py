import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
li = sys.stdin.readline().split()
M = int(input())
answer = sys.stdin.readline().split()
d = dict()

for l in li:
    a = d.get(l,0)
    d[l] = a+1
for an in answer:
    print(d.get(an, 0), end=' ')