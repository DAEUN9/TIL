def hanoi(n, start, center, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, end, center)
        print(start, end)
        hanoi(n-1, center, start, end)

n = int(input())
print(2**n -1)
hanoi(n, 1, 2, 3)
