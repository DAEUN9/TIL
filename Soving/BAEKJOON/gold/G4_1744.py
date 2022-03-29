# 수 묶기
# https://www.acmicpc.net/status?user_id=asd5687&problem_id=1744&from_mine=1

import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

# 0일때 옆이 음수면 묶어줌
# 1일때 냅둠
# 양수일때 옆도 양수면 옆묶어줌
# 음수일때 옆 음수거나 0이면 묶어줌
m_su = []
p_su = []
zeros = []
for i in range(N):
    a = int(input())
    if a==0:
        zeros.append(0)
    elif a>0:
        p_su.append(a)
    else:
        m_su.append(a)
p_su.sort()
m_su.sort(reverse=True)
total = 0
while p_su:
    a = p_su.pop()
    if a == 1:
        total += 1
    elif p_su:
        b = p_su.pop()
        if b == 1:
            total += 1+a
        else:
            total += a*b
    else:
        total += a

while m_su:
    a = m_su.pop()
    if m_su:
        b = m_su.pop()
        total += a*b
    else:
        m_su.append(a)
        break

while zeros:
    a = zeros.pop()
    if m_su:
        b = m_su.pop()
    else:
        break

for m in m_su:
    total += m

print(total)