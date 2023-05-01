def solution(n, s):
    target = s//n
    if target:
        answer = [target]*n
        for i in range(n-1, n-s%n-1, -1):
            answer[i]+=1
    else:
        return [-1]
    return answer