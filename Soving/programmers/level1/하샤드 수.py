def solution(x):
    n = 0
    a = x//10
    b = x%10
    if x%(a+b)==0:
        return True
    else:
        return False