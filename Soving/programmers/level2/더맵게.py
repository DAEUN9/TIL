import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        fir = heapq.heappop(scoville)
        if fir >= K:
            return answer
        if not len(scoville):
            return -1
        sec = heapq.heappop(scoville)
        heapq.heappush(scoville, fir+sec*2)
        answer += 1
    return -1