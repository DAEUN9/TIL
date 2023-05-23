import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())


def solution():
    A = list(map(int, [*input().rstrip()]))
    N = len(A)
    for i in range(N-2, -1, -1):
        for j in range(N-1, i, -1):
            if A[j] > A[i]:
                A[j], A[i] = A[i], A[j]
                return ''.join(map(str, A[:i + 1] + sorted(A[i + 1:])))
    return("BIGGEST")

for _ in range(T):
    print(solution())