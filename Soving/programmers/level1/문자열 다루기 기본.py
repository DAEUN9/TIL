def solution(s):
    answer = True
    for ss in s:
        if '0'<=ss<='9':
            continue
        return False
    if len(s) != 4 and len(s) != 6:
        return False
    return answer