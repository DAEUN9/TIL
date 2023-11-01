def solution(my_string, is_suffix):
    n = len(is_suffix)
    if my_string[-n:] == is_suffix:
        return 1
    return 0