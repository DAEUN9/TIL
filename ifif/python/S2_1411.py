import sys
sys.stdin = open("input.txt", "r")
N = int(input())
words = list(input() for _ in range(N))
answer = 0
def check(a, b):
    d = dict()
    length = len(a)
    for l in range(length):
        if a[l] != b[l]:
            if d.get(a[l], 0) == 0:
                b = b.replace(b[l], a[l])
                d[a[l]] = 1
            else:
                return False
        else:
            d[a[l]] = 1
    if a == b:
        return True
    return False

for i in range(N-1):
    for j in range(i+1, N):
        if check(words[i], words[j]):
            answer += 1

print(answer)