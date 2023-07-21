def solution(s):
    answer = []
    idx = 0
    for ss in s:
        if ss == " ":
            answer.append(" ")
            idx = 0
        elif idx%2 == 0:
            idx += 1
            answer.append(ss.upper())
        else:
            idx += 1
            answer.append(ss.lower())

    return ''.join(answer)