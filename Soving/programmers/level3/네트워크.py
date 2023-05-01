from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        answer += 1
        dq = deque([i])
        while dq:
            curr = dq.popleft()
            for i in range(n):
                if not visited[i] and computers[curr][i]:
                    visited[i] = 1
                    dq.append(i)
    return answer