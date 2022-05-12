# JadenCase 문자열 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(sli):
    answer = ''
    flag = True
    for sl in sli:
        if sl == ' ':
            answer += sl
            flag = True
        elif flag:
            if sl.isdigit():
                answer += str(sl)
            else:
                answer += sl.upper()
            flag = False
        else:
            answer += sl.lower()
    return answer