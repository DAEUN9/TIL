# 이분 그래프
# https://www.acmicpc.net/problem/1707

import sys
sys.stdin =open('input.txt','r')

def find_set(x):
    while parent[x] != x:
        x = parent[x]
    return x

K = int(input())
for k in range(K):
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]
    for e in range(E):
        a, b = map(int, input().split())
