# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541

import sys
sys.stdin = open('input.txt', 'r')
fx = input()
# 플러스
flag = True
total = 0
temp = '0'
for f in fx:
    if flag :
        if f.isdigit():
            temp += f
        else:
            total += int(temp)
            temp = '0'
            if f == '-':
                flag = False
    else:
        if f.isdigit():
            temp += f
        else:
            total -= int(temp)
            temp = '0'
if flag:
    total += int(temp)
else:
    total -= int(temp)
print(total)