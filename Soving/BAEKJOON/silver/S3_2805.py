import sys

# sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

big_tree = max(li)

start = 1
end = big_tree
while start<=end:
    middle = (start+end)//2
    length = 0
    for l in li:
        if l>middle:
            length += l-middle
        if length >M:
            break
    if length < M:
        end = middle-1
    else:
        start = middle+1
print(end)