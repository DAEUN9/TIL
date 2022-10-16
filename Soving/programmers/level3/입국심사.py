# 입국심사
# 이분탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    times.sort()
    start = 1
    end = times[-1] * n
    while start <= end:
        mid = (start + end)//2
        people = 0
        # n동안 심사할 수 있는 사람 수
        for time in times:
            people += mid//time
        # 심사 가능 사람이 더 많으면
        if people >= n:
            end = mid -1
        # 심사 가능 사람이 더 적으면
        else:
            start = mid +1
    return start