# 같은 숫자는 싫어
# 스택/큐
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    curr = arr[0]
    for a in arr[1:]:
        if curr != a:
            answer.append(curr)
        curr = a
    answer.append(arr[-1])
    return answer