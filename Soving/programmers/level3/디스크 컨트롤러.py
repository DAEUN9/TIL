# 디스크 컨트롤러
# https://school.programmers.co.kr/learn/courses/30/lessons/42627


# 요청시점이 작고 이전작업종료 후이며, 작업이 끝나는시간이 작은거 먼저수행
# 작업중에 요청 안들어왔으면 먼저 들어온거부터

import heapq
from collections import deque
#
# # def solution(jobs):
# #     answer = 0
# #     length = len(jobs)
# #     curr = 0
# #     start = 0
# #     while jobs:
# #         heapq.heappop(jobs)
# #         request, time = heapq.heappop(jobs)
# #         if request >= curr:
# #             curr = request+time
#             start = request
#             answer += time
#         else:
#
#
#     answer += time
#
#     return answer

def solution(jobs):
    # tasks를 작업시간, 요청시간으로 만들어서
    # 요청시간 기준으로 정렬
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    # 요청시간이 가장 짧은거 힙에 넣어줌
    heapq.heappush(q, tasks.popleft())
    curr, answer = 0, 0
    # 힙이 빌때까지 반복
    while q:
        # 작업시간, 요청시간
        time, request = heapq.heappop(q)
        # 현재시간+작업시간, 요청시간+작업시간
        # 더 큰게 실제 작업 끝나는시간
        curr = max(curr+time, request+time)
        # 요청부터 걸리는시간 체크
        answer += curr-request
        # 작업중 요청시간이 가장 짧고 현재시간(이전작업끝나는시간) 보다 같거나작으면
        # 힙에 넣어줌
        while tasks and tasks[0][1] <= curr:
            heapq.heappush(q, tasks.popleft())
        # 테스크는 존재하지만 힙이 비었다면
        # 넣어줌
        if tasks and not q:
            heapq.heappush(q, tasks.popleft())
    # 평균 구하기
    return answer // len(jobs)