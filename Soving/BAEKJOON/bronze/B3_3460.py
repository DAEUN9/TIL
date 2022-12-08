# 이진수
# https://www.acmicpc.net/problem/3460

T = int(input())
for _ in range(T):
    n = int(input())
    number = bin(n)[2:][::-1]
    for i, num in enumerate(number):
        if num=="1":
            print(i, end=" ")