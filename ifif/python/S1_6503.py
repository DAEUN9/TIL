import sys
from collections import Counter
sys.stdin = open("input.txt", "r")

while True:
    m = int(input())
    if m == 0:
        break
    s = list(input())
    counter = dict()
    answer = 0
    start = -1
    end = -1
    while start <= end:
        if len(counter) > m:
            start += 1
            counter[s[start]] -= 1
            if counter[s[start]] == 0:
                del counter[s[start]]
        else:
            end += 1
            if end >= len(s):
                break
            temp = counter.get(s[end], 0)
            counter[s[end]] = temp + 1
            if len(counter) <= m:
                answer = max(answer, end-start)

    print(answer)
