def solution(arr):
    a = arr[0]
    for i in arr:
        if a>i:
            a = i
    arr.remove(a)
    if arr==[]:
        arr.append(-1)
    return arr