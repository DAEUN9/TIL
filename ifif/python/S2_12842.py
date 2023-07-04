import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, s = map(int, input().split())
m = int(input())
t_li = [int(input()) for _ in range(m)]

def solution():
    soboros = n-s
    for t in range(100000):
        for i in range(m):
            if t%t_li[i] == 0:
                soboros -= 1
            if not soboros:
                return i+1
    return 1
print(solution())
