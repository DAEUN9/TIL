import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A, B = input().split()
    one_cnt = 0
    zero_cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            if A[i] == '0':
                zero_cnt += 1
            else:
                one_cnt += 1
    change = max(zero_cnt, one_cnt)
    print(change)