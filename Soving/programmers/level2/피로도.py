from itertools import permutations

def solution(k, dungeons):
    answer = 0
    li = [i for i in range(len(dungeons))]
    for order in list(permutations(li, len(dungeons))):
        piro = k
        cnt = 0
        for j in order:
            a, b = dungeons[j]
            if piro >= a:
                piro -= b
                cnt += 1
            answer = max(cnt, answer)
    return answer
    
    
    return answer