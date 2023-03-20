import sys
sys.stdin = open("input.txt", "r")
n = int(input())
start = 0
end = n
while start <= end:
    q = (start+end)//2
    if q**2 >= n:
        end = q-1
    else:
        start = q+1
print(start)