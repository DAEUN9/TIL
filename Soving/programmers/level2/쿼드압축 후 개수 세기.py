answer = [0, 0]

def check(arr):
    target = arr[0][0]
    for ar in arr:
        for a in ar:
            if target != a:
                return False
    return True

def solution(arr):
    N = len(arr)
    target = arr[0][0]
    if N==1 or check(arr):
        answer[target] += 1
        return answer
    solution([arr[i][:N//2] for i in range(N//2)])
    solution([arr[i][N//2:] for i in range(N//2)])
    solution([arr[i][:N//2] for i in range(N//2, N)])
    solution([arr[i][N//2:] for i in range(N//2, N)])

    return answer