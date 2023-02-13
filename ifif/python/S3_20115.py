# 에너지 드링크

# 그리디

import sys

sys.stdin = open("input.txt", "r")
N = int(input())
li = list(map(int, input().split()))
li.sort(reverse=True)
total = li[0]
for l in li[1:]:
    total += l/2

if total%1:
    print(total)
else:
    print(int(total))