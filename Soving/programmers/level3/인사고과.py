def solution(scores):
    rank = 1
    wanho_a, wanho_b, scores = scores[0][0], scores[0][1], scores[1:]
    target = 0
    for a, b in sorted(scores, key=lambda x : (-x[0], x[1])):
        if a > wanho_a and b > wanho_b:
            return -1
        if target <= b:
            target = b
            if a+b > wanho_a+wanho_b:
                rank += 1
    return rank