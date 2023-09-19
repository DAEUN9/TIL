# fees : 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
# records[] : 시각, 차량번호, 내역

import math

def solution(fees, records):
    answer = []
    check = dict()
    prices = dict()
    for record in records:
        time, number, type = record.split()
        minutes = time_to_minutes(time)
        if not prices.get(number):
            prices[number] = 0
        if type == "IN":
            check[number] = minutes
        else:
            prices[number] += minutes - check[number]
            check[number] = -1

    for num, price in sorted(prices.items()):
        if check[num] != -1:
            price += time_to_minutes("23:59") - check[num]
        if price <= fees[0]:
            answer.append(fees[1])
        else:
            temp = 0
            price -= fees[0]
            temp = (math.ceil(price / fees[2])) * fees[3] + fees[1]
            answer.append(temp)
        
    
    return answer

def time_to_minutes(time):
    h, m = map(int, time.split(":"))
    return h*60 + m