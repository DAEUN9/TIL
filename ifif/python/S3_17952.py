import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N = int(input())
stack = []
answer = 0
for i in range(N):
    temp = input()
    if temp[0] == "1":
        t = list(map(int, temp.split()))
        stack.append([t[1], t[2]])
    if stack:
        stack[-1][-1] -= 1
        if stack[-1][-1] == 0:
            answer += stack[-1][0]
            stack.pop()
print(answer)
