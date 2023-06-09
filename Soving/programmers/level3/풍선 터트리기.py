def solution(a):
    if len(a) <= 3:
        return len(a)
    answer = 2
    left_table = [0]*len(a)
    right_table = [0]*len(a)
    left_table[0], right_table[-1] = a[0], a[-1]
    for i in range(1, len(a)):
        left_table[i] = min(left_table[i-1], a[i])
    for k in range(len(a)-2, -1, -1):
        right_table[k] = min(right_table[k+1], a[k])
        
    for j in range(1, len(a)-1):
        if left_table[j-1] < a[j] and right_table[j+1] < a[j]:
            continue
        answer += 1
    return answer