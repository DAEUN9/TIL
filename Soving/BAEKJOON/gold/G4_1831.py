# 댄스 파티
#
# https://www.acmicpc.net/problem/2831
# 그리디 알고리즘
# 정렬
# 두 포인터

import sys
sys.stdin = open("input.txt", "r")
N = int(input())
# 남 키가 양수면 여 키가 큰 여자 원함
# 여자 키가 음수이면서 커야함

# 남 키가 음수면 여 키가 작은 여자 원함
# 여자 키가 양수이면서 작아야 함
man_list = list(map(int, input().split()))
woman_list = list(map(int, input().split()))

ml1 = sorted(man_list, reverse=True)
wl1 = sorted(woman_list, reverse=True)
man_list.sort()
woman_list.sort()
start = 0
end = 0
answer = 0
while start<N and end<N:
    m = man_list[start]
    w = wl1[end]
    if m > 0 or w < 0:
        break
    if m+w < 0:
        start += 1
        end += 1
        answer += 1
    else:
        end += 1

start, end = 0, 0
while start<N and end<N:
    w = woman_list[start]
    m = ml1[end]
    if m < 0 or w > 0:
        break
    if m+w < 0:
        start += 1
        end += 1
        answer += 1
    else:
        end += 1
print(answer)
