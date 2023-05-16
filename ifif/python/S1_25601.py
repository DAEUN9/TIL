import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N = int(input())
cast_dic = dict()
for _ in range(N-1):
    A, B = input().split()
    cast_dic[A] = B
a, b = input().split()
answer = 0
parent = cast_dic.get(a)
while True:
    if parent == b:
        answer = 1
        break
    if cast_dic.get(parent):
        parent = cast_dic[parent]
    else:
        break
if answer:
    pass
else:
    parent = cast_dic.get(b)
    while True:
        if parent == a:
            answer = 1
            break
        if cast_dic.get(parent):
            parent = cast_dic[parent]
        else:
            break
print(answer)