# import sys
#
# sys.stdin = open('input.txt', 'r')

T = int(input())
li = [input() for i in range(T)]
li = set(li)
li = list(li)
answer = []
for l in li:
    answer.append((len(l), l))
answer.sort()
for a in answer:
    print(a[1])