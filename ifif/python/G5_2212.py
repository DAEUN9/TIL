# 센서

# 그리디
# 정렬

import sys

sys.stdin = open("input.txt", "r")

N = int(input())
K = int(input())
li = list(map(int, input().split()))
li.sort()
distance = []
for i in range(N-1):
    distance.append(li[i+1]-li[i])

distance.sort()
print(sum(distance[:N-K]))