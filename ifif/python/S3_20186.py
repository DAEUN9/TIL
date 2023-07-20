import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
print(sum(li[len(li)-K:len(li)])-sum(range(K)))