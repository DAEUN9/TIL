def solution(food):
    answer = ''
    for cnt in range(1, len(food)):
        answer += str(cnt) * (food[cnt]//2)
    
    return answer + '0' + answer[::-1]