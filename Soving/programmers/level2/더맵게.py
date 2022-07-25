import heapq


def solution(scoville, K):
    answer = 0

    while len(scoville)>=2:
        fir = heapq.heappop(scoville)
        if fir >= K:
            return answer
        answer += 1
        if scoville:
            sec = heapq.heappop(scoville)
        heapq.heappush(scoville, fir+sec*2)

    return -1

print(solution([1, 2, 3, 9, 10, 12], 7))