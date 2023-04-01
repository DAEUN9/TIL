def solution(babbling):
    answer = 0
    targets = ["aya", "ye", "woo", "ma"]
    for babbl in babbling:
        cnt = len(babbl)
        for target in targets:
            babbl = babbl.replace(target, "-"*len(target))
        if babbl == "-"*cnt:
            answer += 1
    return answer