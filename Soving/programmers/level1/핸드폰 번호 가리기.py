def solution(phone_number):
    num=len(phone_number)
    answer = ''
    for i in range(num):
        if (num-i)>4:
            answer+='*'
        else:
            answer+=phone_number[i]
        
    return answer