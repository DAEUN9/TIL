import sys
sys.stdin = open("input.txt", "r")
N = int(input())
answer = ""
files = []
for _ in range(N):
    files.append(input())

for j in range(len(files[0])):
    before = files[0][j]
    for i in range(N):
        if files[i][j] == before:
            continue
        answer += "?"
        break
    else:
        answer += before

print(answer)