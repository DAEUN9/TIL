def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    x = len(arr2[0])
    answer = []
    
    for i in range(n):
        temp = []
        for j in range(x):
            curr = 0
            for k in range(m):
                curr += arr1[i][k] * arr2[k][j]
            temp.append(curr)
        answer.append(temp)
            
            
    return answer