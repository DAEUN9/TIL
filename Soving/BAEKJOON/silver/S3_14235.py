# 크리스마스 선물
# https://www.acmicpc.net/problem/14235

import sys
# import heapq


sys.stdin = open('input.txt', 'r')

N = int(input())

# 1번 풀이: 힙큐
# q = []
# for n in range(N):
#     li = input().split()
#     if li == ['0']:
#         if q:
#             print(heapq.heappop(q) * -1)
#         else:
#             print(-1)
#     else:
#         for l in li[1:]:
#             heapq.heappush(q, int(l)*-1)

# 2번 풀이: 정렬해서 팝하기
li = []
for n in range(N):
    present = input().split()
    if present[0] == '0':
        if li:
            print(li.pop())
        else:
            print(-1)
    else:
        for p in present[1:]:
            li.append(int(p))
        li.sort()