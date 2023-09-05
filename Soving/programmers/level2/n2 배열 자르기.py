def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        curr = max(i//n, i%n)
        answer.append(curr+1)
    return answer