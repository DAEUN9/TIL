# 트리 순회
# https://www.acmicpc.net/problem/1991

# import sys
#
# sys.stdin = open('input.txt', 'r')
N = int(input())
d = dict()

for n in range(1,N+1):
    li = input().split()
    d[li[0]] = [li[1], li[2]]

def preorder(v):
    if v != '.':
        print(v,end='')
        preorder(d[v][0])
        preorder(d[v][1])

def inorder(v):
    if v != '.':
        inorder(d[v][0])
        print(v,end='')
        inorder(d[v][1])

def postorder(v):
    if v != '.':
        postorder(d[v][0])
        postorder(d[v][1])
        print(v, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')