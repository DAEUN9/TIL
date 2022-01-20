def solution(s):
    a = 'plus'
    answer = ''
    for i in s:
        if i == '-':
            a = 'minus'
        else:
            answer += i
    answer = int(answer)
    if a == 'minus':
        answer *= -1
    return answer