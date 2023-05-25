from collections import defaultdict
from collections import Counter

def solution(gems):
    answer = [1, len(gems)]
    counter = Counter(gems)
    d = defaultdict(lambda : 0)
    end = 0
    for i, gem in enumerate(gems):
        if i:
            d[gems[i-1]] -= 1
            if not d[gems[i-1]]:
                del d[gems[i-1]]
        while len(d) < len(counter):
            end += 1
            if end > len(gems):
                break
            d[gems[end-1]] += 1
            
        if end-i-1 < answer[1] - answer[0]:
            answer = [i+1, end]
        
    return answer