import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    answer = 0
    max_price = max(prices)
    sells = []
    for i in range(N):
        if prices[i] < max_price:
            sells.append(prices[i])
        else:
            while sells:
                curr = sells.pop()
                answer += max_price - curr
            if i+1 < N:
                max_price = max(prices[i+1:])
    print(answer)