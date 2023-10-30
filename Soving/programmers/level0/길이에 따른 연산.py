from functools import reduce

def solution(num_list):
    N = len(num_list)
    if N >= 11:
        return sum(num_list)
    return reduce(lambda x, y: x*y, num_list)