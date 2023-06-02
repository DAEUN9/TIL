def solution(price, money, count):
    answer = 0
    cnt = 0
    while cnt < count:
        cnt += 1
        answer += price*cnt
    return max(answer-money, 0)