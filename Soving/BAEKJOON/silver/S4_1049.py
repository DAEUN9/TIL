import sys
sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())
min_package = 1e9
min_one = 1e9
for _ in range(M):
    p, o = map(int, input().split())
    min_one = min(min_one, o)
    min_package = min(min_package, p)

a = min_one*N
b = min_package*(N//6)+min_one*(N%6)
c = min_package*(N//6+1)
print(min(a, b, c))