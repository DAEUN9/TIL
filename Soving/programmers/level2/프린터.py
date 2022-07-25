from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for i in range(len(priorities)):
        queue.append([priorities[i], i])
    while queue:
        max_n = 0
        for a, b in queue:
            if a > max_n:
                max_n = a
        curr = queue.popleft()
        if queue and (curr[0] < max_n):
            queue.append(curr)
        else:
            answer += 1
            if curr[1] == location:
                break
    return answer

print(solution([2, 1, 3, 2], 2))