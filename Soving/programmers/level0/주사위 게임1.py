def solution(a, b):
    if a%2 and b%2:
        return a**2 + b**2
    if a%2 or b%2:
        return 2*(a+b)
    return abs(a-b)