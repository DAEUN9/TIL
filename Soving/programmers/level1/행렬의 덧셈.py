def solution(arr1, arr2):
    answer=[]
    
    for i in range(len(arr1)):
        a=[]
        for j in range(len(arr1[0])):
            mat=arr1[i][j]+arr2[i][j]
            a.append(mat)
        answer.append(a)

    return answer