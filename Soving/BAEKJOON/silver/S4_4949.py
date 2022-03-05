import sys

# sys.stdin = open('input.txt', 'r')

while True:
    words = sys.stdin.readline().rstrip()
    if words=='.':
        break
    stack = []
    answer = 'yes'
    for word in words:
        if word in '([':
            stack.append(word)
        elif word == ')':
            if stack:
                a = stack.pop()
                if a != '(':
                    answer = 'no'
            else:
                answer = 'no'
        elif word ==']':
            if stack:
                a = stack.pop()
                if a != '[':
                    answer = 'no'
            else:
                answer = 'no'
    if stack:
        answer ='no'
    print(answer)
