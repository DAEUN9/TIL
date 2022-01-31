T = int(input())
for t in range(T):
    x, y = map(int, input().split())
    length = y - x
    rank = 0
    r = 0
    while rank < length:
        r += 1
        rank = rank+2*r
    if length <= (rank - r):
         print(r*2 - 1)
    else:
         print(r*2)