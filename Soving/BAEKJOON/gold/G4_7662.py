import sys
import heapq

sys.stdin = open('input.txt','r')
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    min_h = []
    max_h = []
    for i in range(k):
        a, b = input().split()
        b = int(b)
        if a == 'I':
            heapq.heappush(min_h, b)
            heapq.heappush(max_h, b*-1)
        elif min_h:
            if b==1:
                x = heapq.heappop(max_h)
                min_h.remove(x*-1)
                # for mi in min_h:
                #     if mi[1] == y:
                #         min_h.remove(mi)
                #         break
            else:
                x = heapq.heappop(min_h)
                max_h.remove(x * -1)
                # for ma in max_h:
                #     if ma[1] == y:
                #         max_h.remove(ma)
                #         break
    if min_h:
        print(heapq.heappop(max_h)*-1, end=" ")
        print(heapq.heappop(min_h))

    else:
        print('EMPTY')
