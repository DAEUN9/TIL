# 프린터 큐
# https://www.acmicpc.net/problem/1966

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    # 1번 풀이
    # N, M = map(int, input().split())
    # li = list(map(int, input().split()))
    # cnt = 0
    # while li:
    #     if li[0] >= max(li):
    #         cnt += 1
    #         if M == 0:
    #             answer = cnt
    #             break
    #         li.pop(0)
    #         M -= 1
    #     elif li[0] < max(li):
    #         if M == 0:
    #             M = len(li) - 1
    #         else:
    #             M -= 1
    #         li.append(li.pop(0))
    #
    # print(cnt)

    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    cnt = 0
    while li:
        curr = li.pop(0)
        if max(li+[0]) <= curr:
            cnt += 1
            if M == 0:
                break
        else:
            li.append(curr)
        M -= 1
        if M < 0:
            M = len(li) - 1
    print(cnt)