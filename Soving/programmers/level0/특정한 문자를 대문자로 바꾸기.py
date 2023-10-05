def solution(my_string, alp):
    answer = ''
    for string in my_string:
        if string == alp:
            answer += string.upper()
        else:
            answer += string
    return answer