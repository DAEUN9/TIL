import sys
sys.stdin = open("input.txt", "r")
N = int(input())
string = input()
before = ''
B_cnt = 0
R_cnt = 0
for s in string:
    if s != before:
        if s == 'B':
            B_cnt +=1
        else:
            R_cnt += 1
    before = s
print(min(B_cnt, R_cnt)+1)