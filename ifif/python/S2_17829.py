import sys
sys.stdin = open("input.txt", "r")
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def pooling(x, y, length):
    temp_arr = []
    if length == 2:
        for i in range(x, x+2):
            for j in range(y, y+2):
                temp_arr.append(matrix[i][j])
        temp_arr.sort()
        return temp_arr[-2]
    length //= 2
    a = pooling(x, y, length)
    b = pooling(x, y+length, length)
    c = pooling(x+length, y, length)
    d = pooling(x+length, y+length, length)
    temp_arr = [a, b, c, d]
    temp_arr.sort()
    return temp_arr[-2]
answer = pooling(0, 0, N)
print(answer)