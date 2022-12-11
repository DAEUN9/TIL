# 별찍기 - 5
# https://www.acmicpc.net/problem/2442

N = int(input())

star_tree = []
for i in range(N):
    star = "*"*(2*i+1)
    star_tree.append(star)

length = len(star_tree[-1])
for s in star_tree:
    star_length = len(s)
    blank = (length - star_length)//2
    print(blank*" ", end="")
    print(s)