def solution(x, n):
    answer=[]
    x1=x
    while len(answer)<n:
        answer.append(x)
        x=x+x1
    return answer