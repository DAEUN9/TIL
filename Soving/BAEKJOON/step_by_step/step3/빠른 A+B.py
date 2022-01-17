import sys

n = input()
n=int(n)
for i in range(n): 
    A,B = map(int,sys.stdin.readline().split())          
    print(A+B)