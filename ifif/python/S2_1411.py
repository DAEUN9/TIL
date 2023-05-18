import sys
sys.stdin = open("input.txt", "r")
N = int(input())
words = list()
answer = 0
for _ in range(N):
    word = input()
    d = dict()
    idx = 1
    temp = []
    for w in word:
        if d.get(w):
            temp.append(d[w])
        else:
            d[w] = idx
            temp.append(d[w])
            idx += 1
    words.append(temp)
for i in range(N-1):
    for j in range(i+1, N):
        if words[i] == words[j]:
            answer += 1

print(answer)