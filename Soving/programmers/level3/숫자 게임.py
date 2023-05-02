def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    for a in A:
        if B[-1] > a:
            B.pop()
            answer += 1
        else:
            B.pop(0)
    return answer