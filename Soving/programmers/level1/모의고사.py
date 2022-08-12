# 모의고사
# 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    an_li = [0, 0, 0]
    person1 = [1, 2, 3, 4, 5] * 8
    person2 = [2, 1, 2, 3, 2, 4, 2, 5] * 5
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4
    answer = []
    idx = -1
    for i in range(len(answers)):
        idx += 1
        if idx >= 40:
            idx = 0
        if answers[i] == person1[idx]:
            an_li[0] += 1
        if answers[i] == person2[idx]:
            an_li[1] += 1
        if answers[i] == person3[idx]:
            an_li[2] += 1
    m = max(an_li)
    k = 0
    for an in an_li:
        k += 1
        if an == m:
            answer.append(k)

    return answer