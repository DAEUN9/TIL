import sys
sys.stdin = open('input.txt', 'r')

k = int(input())

def prime(k):
    x = k
    arr = []
    for i in range(2, k):
        if i**2 > k:
            break

        while x%i == 0:
            arr.append(i)
            x //= i
    if x != 1:
        arr.append(x)
    return arr

arr = prime(k)
print(len(arr))
print(*arr)