# 데이터 구조 및 활용1

#### 1. 모음은 몇 개나 있을까?

```python
def count_vowels(S):
    vowels = 'aeiou' # 모음 문자열로 만듦
    cnt = 0
    for v in vowels: # vowels 순환
        cnt += S.count(v) # v의 count 더하기
    return cnt # 모음의 총 갯수

print(count_vowels('apple'))
print(count_vowels('banana'))
```

#### 2. 문자열 조작

옳지 않은 것 고르기

```
(4)	.strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를 찾아 제거한다.
	특정 문자를 지정하지 않으면 오류가 발생한다.
# error
------------------------------
 # 오류 발생하지 않고 공백 제거
```

### 3.정사각형만 만들기

너비와 높이 두개의 리스트 전달받아 정사각형 넓이 리스트 반환

```python
def only_square_area(l1, l2):
    answer = set() # 중복이 있을 수 있으니 집합으로 선언
    for i in l1: # 첫번째 리스트 순회
        for j in l2: # 두번째 리스트 순회
            if i == j: # 가로, 높이가 같다면
                answer.add(i*j) # 넓이를 answer에 추가
    
    return list(answer) # answer을 list로 바꿔서 반환

print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
```

---

# 데이터 구조 및 활용2

#### 1. 평균 점수 구하기

```python
def get_dict_avg(d):
    length = 0 # d의 길이 구할 값
    score = 0 # 총점 더할 값
    for k in d:# 전달받은 딕셔너리 순회
        score += d[k] # 과목당 점수를 score에 더함
        length += 1 # 길이 1 추가
    return score/length # 총점을 길이로 나눈 값 반환

print(get_dict_avg({
    'python':80,
    'algorithm': 90,
    'django' : 89,
    'web': 83,
    }))
```

#### 2. 혈액형 분류하기

key는 혈액형의 종류, value는 사람 수인 dictionary 반환

```python
def count_blood(bl_li):
    bl = ['A','B','O','AB'] # 혈액형 종류 리스트
    answer = dict() # 정답을 담을 딕셔너리 선언
    for i in bl: # 혈액형 종류 리스트 순회
        cnt = 0 # 카운트 초기화
        for j in bl_li: # 혈액형 정보 리스트 순회
            if i == j: # i 와 j가 같으면
                cnt += 1 # 카운트 추가
                answer[i] = cnt # i에 대한 value를 cnt로
    
    return answer # 딕셔너리 반환

print(count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB',
]))
```

---

# 데이터 구조 및 활용3

#### 1. Built-in 함수와 메서드

sorted()와 .sort()의 차이점을 코드의 실행 결과를 활용하여 설명

```python
# sorted
a = [3, 2, 1]
b= sorted(a)

print(a)
print(b)
-------------------
[3, 2, 1]
[1, 2, 3]


# sort
a = [3, 2, 1]
b= a.sort()

print(a)
print(b)
---------------------
[1, 2, 3]
[1, 2, 3]

''' 
sorted는 원래 리스트를 바꾸지않고 새로운 리스트를 정렬
sort는 원래 리스트를 바꾸고 None값을 반환한다.
'''
```

#### 2. .extend()와 .append()

.extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명

```python
#.extend()
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.extend(['wcafe', '빽다방'])

print(cafe)
------------------------------------
['starbucks', 'tomntoms', 'hollys', 'wcafe', '빽다방']


#.append()
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.append(['wcafe', '빽다방'])

print(cafe)
--------------------------------------
['starbucks', 'tomntoms', 'hollys', ['wcafe', '빽다방']]


'''
append는 형태 그대로 마지막 인덱스에 삽입
edxtend는 리스트를 합친다고 볼 수 있다.
'''
```

### 3. 복사가 잘 된 건가?

a에 list를 담고 b에 a를 할당한 후, a[2] = 5 로 바꾸면 a와 b의 출력결과는?

```
a와 b는 같다
: 얕은 복사가 되어 주소값이 동일하기 때문이다.
```

---

# 데이터 구조 및 활용4

#### 1. 무엇이 중복일까

문자열에서 중복해서 나타난 문자들을 담은 list 반환

```python
def duplicated_letters(S):
    a =dict()
    answer = []
    for i in S:
        a[i] = a.get(i, 0) + 1
    
    for k, v in a.items():
        if v > 1:
            answer.append(k)
    return answer

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))

```

#### 2. 소대소대

문자열을 소문자와 대문자가 번갈아 나타나도록 변환

```python
def low_and_up(S):
    cnt = 0
    answer = ''
    for i in S:
        cnt += 1
    for j in range(cnt):
        if j%2 == 0:
            answer += S[j].lower()
        else:
            answer += S[j].upper()
    return answer

print(low_and_up('apple'))
print(low_and_up('banana'))
```

#### 3. 솔로 천국 만들기

연속적으로 나타나는 숫자는 하나만 남기고 제거한 list 반환(순서유지)

```python
def lonely(li):
    a = li[0]
    b = [a]
    for l in li:
        if l == a:
            continue
        else:
            b.append(l)
        a = l
    return b

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))
```