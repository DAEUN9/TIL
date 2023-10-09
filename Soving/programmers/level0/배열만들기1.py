def solution(n, k):
    answer=[]
    i= n//k 
    for s in range(1,i+1):
        answer.append(s*k)
    return answer