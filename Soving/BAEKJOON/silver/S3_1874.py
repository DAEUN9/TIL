import sys

# sys.stdin = open('input.txt', 'r')

N = int(input())
target = [int(sys.stdin.readline()) for n in range(N)]
stack = []
answer = []
i = 0
for n in range(1, N+1):
    while stack and target[i] == stack[-1]:
        stack.pop()
        answer.append('-')
        i += 1
    stack.append(n)
    answer.append('+')

while stack:
    if stack[-1] == target[i]:
        stack.pop()
        answer.append('-')
        i += 1
        continue
    else:
        break

if i < N-1:
    print('NO')
else:
    for a in answer:
        print(a)