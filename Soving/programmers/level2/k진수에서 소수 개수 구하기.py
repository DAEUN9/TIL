import math

def solution(n, k):
    answer = 0
    number = ''
    while n > 0:
        n, mod = divmod(n, k)
        number = str(mod) + number
    number = number.split('0')
    for num in number:
        if num == '':
            continue
        num = int(num)
        if num <= 1:
            continue
        else:
            for i in range(2, int(math.sqrt(num))+1):
                if num%i == 0:
                    break
            else:
                answer += 1    
                
    
    return answer