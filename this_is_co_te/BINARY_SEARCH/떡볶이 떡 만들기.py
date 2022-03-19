# 떡 개수, 요청한 떡의 길이
N, M = map(int, input().split())
ddeok = list(map(int, input().split()))

def binary_search(target):
    start = 0
    end = max(ddeok)
    while start<=end:
        mid = (start+end)//2
        total = 0
        for d in ddeok:
            curr = d-mid
            if curr > 0:
                total += curr
        if total == target:
            return mid
        elif total > target:
            result = mid
            start = mid+1
        else:
            end = mid-1
    return result
answer = binary_search(M)
print(answer)