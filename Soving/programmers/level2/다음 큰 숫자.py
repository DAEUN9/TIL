def solution(n):
    cnt = format(n, 'b').count('1')
    temp = n+1
    while True:
        temp_cnt = format(temp, 'b').count('1')
        if cnt == temp_cnt:
            return temp
        temp += 1