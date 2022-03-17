# Hashing
# https://www.acmicpc.net/problem/15829

import sys
sys.stdin = open('input.txt','r')

N= int(input())
words = input()
total = 0
idx = 0
for word in words:
    total += ord(word)%96*(31**idx)
    idx += 1

print(total%1234567891)
