# 제어문1

#### 1. 세로로 출력하기

자연수 number을 입력 받아, 1부터 number까지의 수를 세로로 한줄씩 출력

```python

number = int(input("숫자 입력: "))
for i in range(1,number+1):
    print(i)
```



#### 2. 거꾸로 세로로 출력하기

```python
number = int(input("숫자 입력: "))
for i in range(number,0,-1):
    print(i)
```





#### 3. N줄 덧셈

자연수 number을 입력받아 1부터 number까지 모두 더한 수 출력

```python
total=0
number = int(input("숫자 입력: "))
for i in range(1,number+1):
    total+=i
print(total)
```

-----

# 제어문2

#### 1. Mutable & Immutable

주어진 컨테이너들을 각각 변경 가능한 것과 변경 불가능한 것으로 분류

```
mutable: List, Set, Dictionary
immutable: String, Tuple, Range
```

#### 2. 홀수만 담기

range와 slicing을 활용하여 1~50 홀수로만 이루어진 리스트 만들기

```python
l = []
for i in range(1,51,2):
    l.append(i)
print(l)
```

#### 3. Dictionary 만들기

```python
class_mate={'강보경':26, '고광':27, '김다은':24,
 '김성령':26, '박찬석':28,}
print(class_mate.items())
```

#### 4. 반복문으로 네모 출력

```python
n = 5
m = 9

for i in range(m):
    for j in range(n):
        print('*',end='')
    print('')
```

#### 5. 조건 표현식

```python
temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실 가능')
```

#### 6. 평균 구하기

```python
scores = [80, 89, 99, 83]
sum = 0
count = 0
for i in scores:
    sum += i
    count += 1
print(sum/count)
```

---

# 제어문3

#### 1. 간단한 N의 약수 (SWEA #1933)

n의 약수 오름차순으로 출력

```python
N = int(input())
for i in range(1,N+1):
    if N%i==0:
        if N==i:
            print(i,end='')
        else:          
            print(i,end=' ')
    else:
        continue
```

#### 2. 중간값 찾기 (SWEA #2063 변형)

전체의 중앙에 위치하는 수치 출력

```python
numbers = [
           85,72,38,80,69,65,68,96,22,49,67,
           51,61,63,87,66,24,80,83,71,60,64,
           52,90,60,49,31,23,99,94,11,25,24
         ]
j = 0
numbers = sorted(numbers)
print(numbers)
for i in numbers:
    j += 1

if j%2==0:
    print((numbers[j/2]+numbers[j/2-1])/2)

else:
    print(numbers[j//2])
```

#### 3. 계단 만들기

높이가 number인 내려가는 계단 출력

```python
number = int(input())

for i in range(1, number+1):
    for j in range(1, number+1):
        if i == j:
            for k in range(1, i+1):
                if k == i:
                    print(k,end='')
                    break
                else:
                    print(k,end=' ')
    print('')
```

