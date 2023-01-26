import sys

sys.stdin = open("input.txt", "r")
T = int(input())
def solution(d, k):
    if not d:
        return [-1]
    min_num = 1e9
    max_num = 0
    for val in d.values():
        for i in range(len(val)-k+1):
            temp = val[i+k-1] - val[i] + 1
            min_num = min(min_num, temp)
            max_num = max(max_num, temp)
    return min_num, max_num


for _ in range(T):
    W = input()
    K = int(input())
    dic = dict()
    idx = -1
    for w in W:
        idx += 1
        dic.setdefault(w, [])
        dic[w].append(idx)
    for key, value in list(dic.items()):
        if len(value) < K:
            dic.pop(key)
    print(*solution(dic, K))
