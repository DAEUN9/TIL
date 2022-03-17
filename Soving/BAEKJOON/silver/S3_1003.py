# 피보나치 함수
# https://www.acmicpc.net/problem/1003

# import sys

# sys.stdin = open('input.txt', 'r')

fibo_arr = list([0, 0] for _ in range(41))
def fibo(n):
    if n == 0:
        fibo_arr[n][0] = 1
        return fibo_arr[n]
    if n == 1:
        fibo_arr[n][1] = 1
        return fibo_arr[n]
    if fibo_arr[n][0] and fibo_arr[n][1]:
        return fibo_arr[n]
    fibo_arr[n] = [fibo(n-1)[0]+fibo(n-2)[0], fibo(n-1)[1]+fibo(n-2)[1]]
    return fibo_arr[n]

T = int(input())
li = []
for t in range(T):
    li.append(int(input()))
for l in li:
    fibo(l)
    print(fibo_arr[l][0], fibo_arr[l][1])
