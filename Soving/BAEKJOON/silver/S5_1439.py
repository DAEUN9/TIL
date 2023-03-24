import sys
sys.stdin = open("input.txt", "r")
S = input()
before = S[0]
one_cnt = 0
zero_cnt = 0
for s in S[1:]:
    if before=="0" and s=="1":
        one_cnt += 1
    elif before=="1" and s=="0":
        zero_cnt += 1
    before = s
print(max(one_cnt, zero_cnt))