# 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque


def bfs(del_line, n, wires_array):
    count = 1  # 연결 노드 수
    visited = [False] * (n + 1)
    visited[del_line[0]] = True
    queue = deque([del_line[0]])

    while queue:
        curr = queue.popleft()
        for i in wires_array[curr]:
            if visited[i] or i == del_line[1]: 
                continue
            count += 1
            queue.append(i)
            visited[i] = True
    return count


def solution(n, wires):
    answer = 1e9
    array = [[]*(n+1) for _ in range(n+1)]
    for a, b in wires:
        array[a].append(b)
        array[b].append(a)

    for w in wires:
        # w 끊을 와이어
        temp = bfs(w, n, array)
        answer = min(answer, abs(temp - (n-temp)))
    return answer