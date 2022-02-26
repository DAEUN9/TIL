# import sys
#
# sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    li = input().split()
    shuffle = [0]*N

    i = -2
    for l in li[:N//2+N%2]:
        i += 2
        shuffle[i] = l

    j = -1
    for l in li[N//2+N%2:]:
        j += 2
        shuffle[j] = l

    print(f'#{t}', *shuffle)