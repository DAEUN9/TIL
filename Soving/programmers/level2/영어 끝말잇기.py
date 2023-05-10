def solution(n, words):
    d = dict()
    cicle = 1
    before = words[0][0]
    while words:
        for i in range(n):
            if len(words) == 0:
                return [0, 0]
            curr = words.pop(0)
            if before[-1] != curr[0]:
                return [i+1, cicle]
            if d.get(curr):
                return [i+1, cicle]
            d[curr] = 1
            before = curr
        cicle += 1
    

    return [0, 0]