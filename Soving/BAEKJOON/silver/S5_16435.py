import sys
sys.stdin = open("input.txt", "r")
N, L = map(int, input().split())
fruits = list(map(int, input().split()))
fruits.sort()
for fruit in fruits:
    if fruit <= L:
        L += 1
print(L)