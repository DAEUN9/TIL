# 피보나치 수 2
#
# 수학
# 다이나믹 프로그래밍

import sys
sys.stdin = open("input.txt", "r")

n = int(input())
fibo = [0, 1]
for i in range(2, n+1):
    fibo.append(fibo[i-1] + fibo[i-2])

print(fibo[-1])