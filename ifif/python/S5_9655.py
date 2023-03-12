import sys
sys.stdin = open("input.txt", "r")
N = int(input())
if N%2:
    print("SK")
else:
    print("CY")