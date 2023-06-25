import sys
sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
arr = list(list(input()) for _ in range(n))
min_row, min_col = n, m
for i in range(n):
    curr = 1
    for j in range(m-1):
        if arr[i][j] == arr[i][j+1]:
            curr += 1
            if j == m-2:
                min_col = min(min_col, curr)
        else:
            min_col = min(min_col, curr)
            curr = 1
            if j == m-2:
                min_col = min(min_col, curr)

for j in range(m):
    curr = 1
    for i in range(n-1):
        if arr[i][j] == arr[i+1][j]:
            curr += 1
            if i == n-2:
                min_row = min(min_row, curr)
        else:
            min_row = min(min_row, curr)
            curr = 1
            if i == n-2:
                min_row = min(min_row, curr)
print(n//min_row, m//min_col)
for i in range(0, n, min_row):
    temp = ''
    for j in range(0, m, min_col):
        temp += arr[i][j]
    print(temp)