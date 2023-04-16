import sys
sys.stdin = open("input.txt", "r")
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
curr = 1
for i in range(1, 100000):
    curr *= 2
    if curr >= numbers[-1]:
        print(i)
        break