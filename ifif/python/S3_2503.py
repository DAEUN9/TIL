# 숫자 야구
# 구현, 브루트포스

import sys

sys.stdin = open("input.txt", "r")
T = int(input())
answer = set(str(i) for i in range(1, 10))
stList = [set(),set(),set()]
ballList = set()
for _ in range(T):
    N, st, ball = map(int, input().split())
    numList = list(str(N))
    if st ==0 and ball ==0:
        for num in numList:
            answer.remove(num)
        continue
    if st:
        for i in range(3):
            stList[i].add(numList[i])
    if ball:
        ballList.update(set(numList).intersection(answer))
print(ballList)
print(stList)