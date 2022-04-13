# 리모컨
# https://www.acmicpc.net/problem/1107

import sys
sys.stdin = open('input.txt', 'r')

# 이동하려는 채널
N = int(input())
# 고장난 버튼 개수
M = int(input())
# 버튼 리스트
button = set([i for i in range(10)])
li = set()
if M:
    li = set(map(int, input().split()))
button -= li
min_v = abs(N - 100)
for n in range(1000001):
    for i in str(n):
        if int(i) not in button:
            break
    else:
        min_v = min(min_v, abs(N - n) + len(str(n)))

if M==0:
    min_v = min(len(str(N)), min_v)
print(min_v)