def solution(participant, completion):
    d = dict()
    di = dict()
    for c in participant:
        d[c] = d.get(c, 0) + 1
        di[c] = di.get(c, 0)
    for a in completion:
        di[a] += 1

    for com in participant:
        if d[com] != di[com]:
            return com