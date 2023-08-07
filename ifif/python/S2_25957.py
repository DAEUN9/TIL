import sys
sys.stdin = open("input.txt", "r")

N = int(input())
d = dict()
answer = ''
for _ in range(N):
    words = list(input())
    if len(words) <= 1:
        key = words[0]
    else:
        key = words[0] + ''.join(sorted(words[1:-1])) + words[-1]
    d[key] = ''.join(words)
M = int(input())
S = list(input().split())

for s in S:
    word = list(s)
    if len(word) <= 1:
        key = word[0]
    else:
        key = word[0] + ''.join(sorted(word[1:-1])) + word[-1]
    answer += d[key] + ' '
print(answer)