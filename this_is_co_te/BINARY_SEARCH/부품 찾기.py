N = int(input())
total_li = list(map(int, input().split()))
total_li.sort()
M = int(input())
request = list(map(int, input().split()))

def binary_search(x):
    start = 0
    end = len(total_li)-1
    while start<=end:
        mid = (start+end)//2
        if total_li[mid] == x:
            return True
        elif total_li[mid] < x:
            start = mid+1
        else:
            end = mid-1
    return False

for re in request:
    if binary_search(re):
        print('yes', end=' ')
    else:
        print('no', end=' ')