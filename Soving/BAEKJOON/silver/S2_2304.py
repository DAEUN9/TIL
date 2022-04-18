import sys
sys.stdin = open('input.txt','r')

pillow = []
N = int(input())
for n in range(N):
    L, H = map(int,input().split())
    pillow.append((L, H))
pillow.sort()
curr, heigh = pillow[0][0], pillow[0][1]
total = 0
for l, h in pillow[1:]:
    if h>heigh:
        total += abs(l-curr)*heigh
        curr, heigh = l, h
m_l, m_h = curr, heigh
curr, heigh = pillow[-1][0]+1, pillow[-1][1]
for l, h in pillow[::-1][1:]:
    if h > heigh:
        total += abs(l+1-curr)*heigh
        curr, heigh = l+1, h
total += (curr-m_l)*m_h

print(total)