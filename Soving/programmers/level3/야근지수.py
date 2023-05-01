import heapq

def solution(n, works):
    hq = []
    answer = 0
    for work in works:
        heapq.heappush(hq, -work)
    for i in range(n):
        temp = heapq.heappop(hq)
        if temp == 0:
            return 0
        heapq.heappush(hq, temp+1)
    for h in hq:
        answer += h**2
    return answer