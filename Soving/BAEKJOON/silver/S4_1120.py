import sys
sys.stdin = open("input.txt", "r")
A, B = input().split()
if len(A) > len(B):
    A, B = B, A
def compare (A, B):
    cnt = 0
    for idx in range(len(A)):
        if A[idx] != B[idx]:
            cnt += 1
    return cnt
answer = 1e9
for i in range(len(B)-len(A)+1):
    cnt = compare(A, B[i:i+len(A)])
    answer = min(answer, cnt)
print(answer)