# 수 이어가기

number = int(input())

result = []
mn = 2
for num in range(1, number+1):
    answer = [number, num]   
    i = 2
    while True:
        a = answer[i-2] - answer[i-1]
        if a < 0:
            break
        answer.append(a)
        i += 1
    if i > mn:
        mn = i
        result = answer[:]
    
result = list(map(str, result))
print(mn)
print(' '.join(result))


