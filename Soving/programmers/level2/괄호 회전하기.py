from collections import deque

d = {
    "]" : "[",
    "}" : "{",
    ")" : "("
}

def solution(s):
    answer = 0
    s = deque(list(s))
    for i in range(len(s)):
        s.rotate(-1)
        if check_correct(s):
            answer += 1
    
    return answer

def check_correct(string):
    stack = []
    for s in string:
        if s in "[{(":
            stack.append(s)
        elif not stack:
            return False
        else:
            curr = stack.pop()
            if curr != d[s]:
                return False
    if stack:
        return False
    return True