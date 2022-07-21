from collections import deque


def solution(progresses, speeds):
    dq = deque()
    answer = []
    for i in range(len(progresses)):
        dq.append([progresses[i], speeds[i]])
    visited = [0]*len(dq)

    flag = True
    curr = 0
    cnt = 0
    while flag:

        flag = False
        for d in range(len(dq)):
            if visited[d]:
                continue
            flag = True
            dq[d][0] += dq[d][1]
            if dq[d][0]>=100:
                cnt += 1
                visited[d] = 1
                if curr == d:
                    curr += 1
                    answer.append(cnt)
                    cnt = 0

    return answer

a = [93, 30, 55]
b = [1, 30, 5]
print(solution(a, b))