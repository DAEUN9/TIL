import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
N = int(input())
d = deque()
for n in range(N):
    word = sys.stdin.readline().split()
    if word[0] == 'push_front':
        d.appendleft(word[1])
    elif word[0] == 'push_back':
        d.append(word[1])
    elif word[0] == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif word[0] == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif word[0] == 'size':
        print(len(d))
    elif word[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif word[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    else:
        if d:
            print(d[-1])
        else:
            print(-1)
