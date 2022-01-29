# 스위치 켜고 끄기

# 남학생: 스위치 번호가 자기가 받은 수의 배수이면 스위치 상태를 바꿈
# 여학생: 받은수와 같은 스위치 번호 중심으로 대칭이면 그 구간 모두 바꿈. 대칭아니면 혼자만

N = int(input())
status = list(map(int,input().split()))
students = int(input())
for student in range(students):
    gender, number = input().split()
    gender, number = int(gender), int(number)
    if gender == 1:
        for i in range(1, N+1):
            if i%number==0:
                status[i-1] = int(not(status[i-1]))
    else:
        girl = [number-1]
        j = 1
        while True:
            if N <= 2:
                break
            if number-j < 1:
                break
            elif number+j > N:
                break 
            elif status[number-1-j] != status[number-1+j]:
                break
            girl.append(number-1-j)
            girl.append(number-1+j)
            j += 1
        for g in girl:
            status[g] = int(not(status[g]))
status = list(map(str, status))
length = len(status)
for k in range(1,length+1):
    if k%20 == 0:
        print(status[k-1],end='')
        print()
        continue
    print(status[k-1],end=' ')