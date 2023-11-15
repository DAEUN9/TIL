def solution(myString):
    answer = ''
    for s in myString:
        if s == "a":
            answer += "A"
        elif s == "A":
            answer += "A"
        else:
            answer += s.lower()
    return answer
