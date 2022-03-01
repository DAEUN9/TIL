
N = int(input())
li = list(map(int, input().split()))
li.sort()
M = int(input())
target = list(map(int, input().split()))

for t in target:
    start = 0
    end = N - 1
    while start<=end:
        middle = (start+end)//2
        if li[middle] == t:
            print('1')
            break
        elif li[middle] > t:
            end = middle -1
        else:
            start = middle +1
    else:
        print('0')