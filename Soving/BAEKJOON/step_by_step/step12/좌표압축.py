import sys

# sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
answer = sorted(li)
d = {answer[0]:0}
before = answer[0]
i = 0
for a in answer[1:]:
    if a == before:
        continue
    else:
        i += 1
        d[a] = i
        before = a
for l in li:
    print(d[l], end=' ')


