# Z
# https://www.acmicpc.net/status?from_mine=1&problem_id=1074&user_id=asd5687

import sys

sys.stdin = open('input.txt', 'r')
input=sys.stdin.readline

n,r,c=map(int,input().split())
ans=0

def solve(x,y,n):
    global ans, flag
    if flag:
        return
    if x==r and y==c:
        flag= True
        return
    if n==1:
        ans+=1
        return
    if not (x<=r<x+n and y<=c<y+n):
        ans+=n*n
        return
    temp=n//2
    solve(x,y,temp)
    solve(x,y+temp,temp)
    solve(x+temp,y,temp)
    solve(x+temp,y+temp,temp)
flag = False
solve(0,0,2**n)
print(ans)