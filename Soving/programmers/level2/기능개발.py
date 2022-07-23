from collections import deque


def solution(progresses, speeds):
    dq = deque()
    answer = []
    for i in range(len(progresses)):
        dq.append([progresses[i], speeds[i]])
    visited = [-1]*len(dq)

    curr = 0

    while sum(visited):
        cnt = 0
        flag = False
        for d in range(len(dq)):
            if visited[d]==0:
                continue
            dq[d][0] += dq[d][1]
            if d == curr and dq[d][0]>=100:
                flag = True
                curr += 1
        if flag:
            for q in range(len(dq)):
                if visited[q] < 0 and dq[q][0]>=100:
                    cnt += 1
                    visited[q] = 0
            answer.append(cnt)

    return answer

a = [95, 90, 99, 99, 80, 99]
b = [1, 1, 1, 1, 1, 1]
print(solution(a, b))