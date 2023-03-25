import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    answer = 0
    max_num = 0
    for i in range(N-1, -1, -1):
        if max_num > prices[i]:
            answer += max_num - prices[i]
        else:
            max_num = prices[i]

    print(answer)