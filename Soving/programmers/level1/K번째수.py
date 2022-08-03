# 정렬
# K번째수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    answer = []
    for i, j, k in commands:
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer