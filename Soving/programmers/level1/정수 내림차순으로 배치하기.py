def solution(n):
    a = ''
    answer = str(n)
    answer = sorted(answer)
    for i in answer:
        a = i+a
    return int(a)