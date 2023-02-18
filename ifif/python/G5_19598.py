# 최소 회의실 개수
#
# 자료 구조
# 그리디 알고리즘
# 정렬
# 스위핑
# 우선순위 큐

import sys
import heapq

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N = int(input())
rooms = [list(map(int, input().split())) for _ in range(N)]
rooms.sort()
# cnt = 0
# while rooms:
#     time = 0
#     temp = []
#     for s, e in rooms:
#         if time<=s:
#             time = e
#         else:
#             temp.append([s, e])
#     cnt+=1
#     rooms = temp
# print(cnt)]

answer = [rooms[0][1]]
for s, e in rooms[1:]:
    temp = heapq.heappop(answer)
    if temp <= s:
        heapq.heappush(answer, e)
    else:
        heapq.heappush(answer, temp)
        heapq.heappush(answer, e)
# print(answer)
print(len(answer))