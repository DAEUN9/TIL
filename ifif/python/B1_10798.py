import sys

sys.stdin = open("input.txt","r")
T = 5
words = [input() for _ in range(T)]
max_len = 0
for word in words:
    if max_len < len(word):
        max_len = len(word)
answer = ""
for i in range(max_len):
    for j in range(5):
        if len(words[j]) > i:
            answer += words[j][i]
print(answer)