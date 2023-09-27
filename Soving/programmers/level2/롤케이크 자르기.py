def solution(topping):
    answer = 0
    d = dict()
    young = dict()
    for to in topping:
        if d.get(to):
            d[to] += 1
        else:
            d[to] = 1
    for t in topping:
        d[t] -= 1
        if d[t] == 0:
            del d[t]
        young[t] = 1
        if len(d) == len(young):
            answer += 1
                
    return answer