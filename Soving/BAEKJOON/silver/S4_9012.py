import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

for n in range(N):
    li = sys.stdin.readline()
    stack=[]
    answer = 'YES'
    for l in li:
        if l == '(':
            stack.append(l)
        elif l == ')':
            if stack:
                a = stack.pop()
                if a !='(':
                    answer='NO'
            else:
                answer='NO'
    if stack:
        answer ='NO'
    print(answer)