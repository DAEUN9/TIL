import sys
sys.stdin = open("input.txt", "r")
n = int(input())
cards = list(map(int, input().split()))
print(sum(cards) + max(cards)*(n-2))