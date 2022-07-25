from collections import deque


# def solution(progresses, speeds):
#     dq = deque()
#     answer = []
#     for i in range(len(progresses)):
#         dq.append([progresses[i], speeds[i]])
#     visited = [-1]*len(dq)
#
#     curr = 0
#
#     while sum(visited):
#         cnt = 0
#         flag = False
#         for d in range(len(dq)):
#             if visited[d]==0:
#                 continue
#             dq[d][0] += dq[d][1]
#             if d == curr and dq[d][0]>=100:
#                 flag = True
#                 curr += 1
#         if flag:
#             for q in range(len(dq)):
#                 if visited[q] < 0 and dq[q][0]>=100:
#                     cnt += 1
#                     visited[q] = 0
#             answer.append(cnt)
#
#     return answer
def solution(progresses, speeds):
    answer = []

    # 모두 배포될때까지
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
        # 우선 기능이 완료되면 배포
        # 후순위 기능도 완료된 상태면 배포
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        # 배포 몇개됐는지
        if cnt > 0:
            answer.append(cnt)
    return answer
a = [95, 90, 99, 99, 80, 99]
b = [1, 1, 1, 1, 1, 1]
print(solution(a, b))