# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# DFS/BFS

from collections import deque

def solution(begin, target, words):
    # 타겟어 없는 경우
    if target not in words:
        return 0

    q = deque()
    q.append([begin, 0])

    while q:
        x, cnt = q.popleft()

        # 타겟이 되면 출력
        if x == target:
            return cnt

        for i in range(0, len(words)):
            diff = 0
            word = words[i]
            for j in range(len(x)):
                if x[j] != word[j]:
                    diff += 1
            # 현재 글자와 한글자만 다르면 q에 추가
            if diff == 1:
                q.append([word, cnt + 1])
    # 큐가 빌 때까지 타겟을 찾을 수 없음
    return 0