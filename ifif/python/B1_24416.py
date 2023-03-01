# 알고리즘 수업 - 피보나치 수 1
#
# 수학
# 다이나믹 프로그래밍

import sys
sys.stdin = open("input.txt", "r")
n = int(input())

def fibonacci(n):
    global b
    f = [0]*(n+1)
    f[1], f[2] = 1, 1
    for i in range(3, n+1):
        b += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]
b = 0

print(fibonacci(n), b)