import sys

# sys.stdin = open('input.txt', 'r')

T = int(input())
stack = []
for t in range(1, T+1):
    word = sys.stdin.readline().split()

    if word[0] == 'push':
        stack.append(word[1])
    elif word[0] == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif word[0] == 'size':
        print(len(stack))
    elif word[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    else:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)