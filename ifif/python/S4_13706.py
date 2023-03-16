import sys
sys.stdin = open("input.txt", "r")
N = int(input())
start = 1
end = N
while start <= end:
    curr = (start + end)//2
    if curr**2 == N:
        print(curr)
        break
    if curr**2<N:
        start = curr
    else:
        end = curr
