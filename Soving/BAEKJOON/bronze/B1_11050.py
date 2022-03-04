N, K = map(int, input().split())

# N!/(N-K)!(K)!

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

answer = factorial(N) // (factorial(N-K) * factorial(K))
print(answer)