def solution(str_list, ex):
    answer = ''
    for s in str_list:
        if ex in s:
            continue
        answer += s
    return answer
