import sys
sys.stdin = open("input.txt", "r")

S = list(input())
one_cnt = 0
zero_cnt = 0
for s in S:
    if s == '0':
        zero_cnt += 1
    else:
        one_cnt += 1

zero_cnt //= 2
one_cnt //= 2
idx = 0
while one_cnt:
    if S[idx] == "1":
        S[idx] = ""
        one_cnt -= 1
    idx += 1

idx = -1
while zero_cnt:
    if S[idx] == "0":
        S[idx] = ""
        zero_cnt -= 1
    idx -= 1
print("".join(S))