import sys
sys.stdin = open("input.txt", "r")

def solution():
    word = input()
    d = dict()
    temp = []
    for i in range(97, 97+26):
        d[chr(i)] = 1
    for idx, w in enumerate(word):
        del d[w]
        temp.append(w)
    keys = sorted(d.keys())
    if keys:
        temp.append(keys[0])
        return ''.join(temp)
    else:
        before = []
        while temp:
            a = temp.pop()
            before.sort()
            for b in before:
                if b > a:
                    temp.append(b)
                    return ''.join(temp)
            before.append(a)
    return -1

print(solution())