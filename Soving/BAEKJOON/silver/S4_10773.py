import sys
# sys.stdin = open('input.txt', 'r')

K = int(input())
total = 0
stack = []
for k in range(K):
    a = int(sys.stdin.readline())
    if a:
        stack.append(a)
    else:
        stack.pop()
print(sum(stack))
