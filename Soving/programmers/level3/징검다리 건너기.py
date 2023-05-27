def solution(stones, k):
    answer = 0
    start, end = 1, max(stones)
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for stone in stones:
            if stone < mid:
                cnt += 1
                if cnt >= k:
                    end = mid-1
                    break
            else:
                cnt = 0
        else:
            if answer < mid:
                answer = mid
            start = mid+1    
        
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, 3))