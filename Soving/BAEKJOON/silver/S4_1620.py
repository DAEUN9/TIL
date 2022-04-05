# 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620

import sys
sys.stdin = open('input.txt', 'r')

# 포켓몬 개수, 문제 개수
input = sys.stdin.readline
N, M = map(int, input().split())
pod = dict()
pol = [0]
for i in range(1,N+1):
    a = input().rstrip('\n')
    pod[a] = i
    pol.append(a)
for m in range(M):
    b = input().rstrip('\n')
    if b.isdigit():
        print(pol[int(b)])
    else:
        print(pod[b])