# https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    cash = []
    answer = 0
    length = len(cities)
    for l in range(length):
        cities[l] = cities[l].lower()

    if cacheSize:
        for city in cities:
            if len(cash) == cacheSize:
                if city in cash:
                    cash.remove(city)
                    cash.append(city)
                    answer += 1
                else:
                    cash.pop(0)
                    cash.append(city)
                    answer += 5
            else:
                if city in cash:
                    cash.remove(city)
                    answer += 1
                else:
                    answer += 5
                cash.append(city)
    else:
        for city in cities:
            answer += 5
    return answer