import heapq


def solution(scoville, K):
    answer = 0
    # 스코빌지수 힙큐로 바꾸기
    heapq.heapify(scoville)
    while True:
        # 가장 맵지 않은 음식의 스코빌지수
        fir = heapq.heappop(scoville)
        # 모든 음식 스코빌지수가 K이상이면 리턴
        if fir >= K:
            return answer
        # 남은 음식이 없으면
        # K이상으로 만들 수 없어서 -1 리턴
        if not len(scoville):
            return -1
        # 두번째로 맵지 않은 음식
        sec = heapq.heappop(scoville)
        # 새로 만든 음식을 힙에 넣는다
        heapq.heappush(scoville, fir+sec*2)
        # 섞기 횟수 += 1
        answer += 1