# 컨베이어 벨트 위의 로봇
# https://www.acmicpc.net/problem/20055

import sys
from collections import deque
sys.stdin = open('input.txt','r')

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0]*N)
zero_cnt = 0
answer = belt.count(0)
while zero_cnt < K:
    robot.rotate(1)
    robot[0] = 0
    robot[-1] = 0
    belt.rotate(1)
    for i in range(N-2, -1, -1):
        if robot[i] and belt[i+1] and not robot[i+1]:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
            if belt[i+1] == 0:
                zero_cnt += 1
            if i == N-2:
                robot[i+1] = 0
    if belt[0]:
        belt[0] -= 1
        robot[0] = 1
        if belt[0] == 0:
            zero_cnt += 1
    answer += 1

print(answer)