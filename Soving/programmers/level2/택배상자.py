from collections import deque

def solution(order):
    answer = 0
    stack = deque()
    curr = 0
    d = dict()
    for i in range(len(order)):
        d[order[i]-1] = i+1
    for o in range(len(order)):
        while stack and curr+1 == d[stack[-1]]:
            temp = stack.pop()
            curr += 1
            answer += 1
        if curr+1 == d[o]:
            answer += 1
            curr += 1
            while stack and curr+1 == d[stack[-1]]:
                temp = stack.pop()
                curr += 1
                answer += 1
        else:
            stack.append(o)    
    
    return answer