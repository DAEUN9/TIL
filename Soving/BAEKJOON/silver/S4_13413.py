import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    black = 0
    white = 0
    curr = list(input())
    target = list(input())
    for a, b in zip(curr, target):
        if a == b:
            continue
        if a == 'W':
            white += 1
        else:
            black += 1
    if white >= black:
        print(white)
    else:
        print(black)