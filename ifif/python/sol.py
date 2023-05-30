import sys
sys.stdin = open("input.txt", "r")

R, C, W = map(int, input().split())
pascal = [[1]]
for i in range(1, R+W+1):
    temp = [1]
    for j in range(1, i):
        temp.append(pascal[i-1][j-1] + pascal[i-1][j])
    pascal.append(temp + [1])

cnt = 0
answer = 0
for i in range(R-1, R+W-1):
    cnt += 1
    answer += sum(pascal[i][C-1:C+cnt-1])
print(answer)