# 데이터 구조





## 순서가 있는 데이터 구조

### 문자열(string)

> immutable, ordered, iterable





#### 조회/탐색

- `.find(x)` : x의 첫 번째 위치를 반환, 만일 x가 없으면, `-1`을 반환

- `.index(x)` : x의 첫 번째 위치를 반환, 만일 x가 없으면, 오류 발생

- `.startswith(x)` : 문자열이 x로 시작하면 True 반환, 아니면 False 반환

- `.endswith(x)` : 문자열이 x로 끝나면 True 반환, 아니면 False 반환





#### 기타 문자열 관련 검증 메서드

- `.isalpha()` : 문자열이 (숫자가 아닌)글자로 이루어져 있는가?
- `.isspace()` : 문자열이 공백으로 이루어져 있는가?
- `.isupper()` : 문자열이 대문자로 이루어져 있는가?
- `.istitle()` : 문자열이 타이틀 형식으로 이루어져 있는가?
- `.islower()` : 문자열이 소문자로 이루어져 있는가?





#### 숫자 판별 메서드

`.isdecimal()` < `.isdigit()` < `.isnumeric()`





#### 문자열 변경

- `.replace(old, new[, count])` : 바꿀 글자를 새로운 글자로 바꿔서 반환, count를 지정하면 해당 개수만큼만 시행

- `.strip([chars])` : 특정한 문자들을 지정하면, 양쪽을 제거하거나(`strip`), 왼쪽을 제거하거나(`lstrip`), 오른쪽을 제거(`rstrip`)

  `chars` 를 지정하지 않으면 공백을 제거

- `.split([chars])` : 문자열을 특정한 단위로 나누어 리스트로 반환

  `chars`를 지정하지 않으면 공백을 기준으로 나눔

- `'separator'.join(iterable)` : iterable 문자열들을 separator로 이어붙인 문자열 반환

  ```python
  words = ['안녕', 'hello']
  ' '.join(words)
  ---------------------------
  안녕 hello
  ```

- `.capitalize()` : 첫글자를 대문자로 만들어 반환
- `.title()` : 어포스트로피(') 나 공백 이후를 대문자로 만들어 반환
- `.upper()` : 모두 대문자로 만들어 반환
- `.lower()` : 모두 소문자로 만들어 반환
- `.swapcase()` : 대 <-> 소문자로 변경하여 반환

***





### 리스트(List)

> mutable, ordered, iterable





#### 값 추가 및 삭제

- `.append(x)` : 리스트에 값을 추가
  - `a[len(a):] = [x]` 와 동일
- `.extend(iterable)` : 리스트에 iterable(list, range, tuple, string) 값을 붙일 수 있음
  - `a[len(a):] = iterable` 와 동일
  - `+=` 연산자와 동일

- `.insert(i, x)` : 정해진 위치 `i` 에 값을 추가
  - 리스트의 길이를 넘어서는 인덱스는 마지막에 아이템 추가

- `.remove(x)` : 리스트에서 값이 x인 첫번재 항목 삭제, 없으면 `ValueError` 발생
- `.pop([i])` : 정해진 위치 `i` 에 있는 값 삭제 후 반환, `i` 없으면 마지막 항목 삭제 후 반환
- `.clear()` : 리스트의 모든 항목을 삭제





#### 탐색 및 정렬

- `.index(x)` : x 값을 찾아 해당 index 값 반환, 없으면 `ValueError` 발생

- `.count(x)` : 원하는 값의 개수 반환

- `.sort()` : 리스트 정렬, 원본 list를 변형시키고, `None` 리턴, 파라미터로는 `key` 와 `reverse` 가 있다.

  - `key`는 함수. 함수 기준으로 정렬 가능

  ```python
  # 정순 정렬
  lotto.sort()
  # 역순 정렬
  lotto.sort(reverse =True)
  ```

- `.reverse()` : 정렬하는 것이 아닌 원본 순서를 뒤집고 수정, `None` 을 리턴.

  파라미터 `key` 와 `reverse` 가 있다.





----

### 튜플(tuple)

> immutable





#### 탐색

- `.index(x[, start[, end]])` : 튜플에 있는 항목 중 값이 x와 같은 첫 번째 인덱스 돌려줌, 값이 없으면 `ValueError` 발생
- `.count(x)` : 튜플에서 x 가 등장하는 횟수 돌려줌





---

## 순서가 없는 데이터 구조

### 셋(set)

> mutable, unordered, iterable





#### 추가 및 삭제

- `.add(elem)` : elem을 셋(set)에 추가

- `.update(*others)` : 여러 값을 추가, 반드시 iterable 데이터 구조를 전달해야함

  ```python
  a = {'사과', '바나나', '수박'}
  a.update({'토마토','토마토','딸기'},{'포도','레몬'})
  print(a)
  ------------------------------------------------------
  {'사과', '바나나', '토마토', '레몬', '포도', '수박', '딸기'}
  ```

- `.remove(elem)` : `elem`을 셋(set)에서 삭제, elem이 존재하지 않으면 `KeyError` 발생
- `.discard(elem)` : `elem`을 셋(set)에서 삭제, elem이 존재하지 않아도 에러 발생X





### 딕셔너리(Dictionary)

> mutable, unordered, iterable
>
> `Key: Value` 페어(pair)의 자료구조





#### 조회

- `.get(key[, default])` : key를 통해 value를 가져옴. key가 존재하지 않으면 default 반환(없으면 None)

- `.setdefault(key[, default])` : key를 통해 value 돌려줌. key가 존재하지 않으면 default 값을 갖는 key를 삽입한 후 default 반환(없으면 None)

  ```python
  my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
  my_dict.setdefault('pineapple','파인애플')
  print(my_dict)
  -------------------------------------------------------
  {'apple': '사과', 'banana': '바나나', 'melon': '멜론', 'pineapple': '파인애플'}
  ```





#### 추가 및 삭제

- `.pop(key[, default])` : key가 딕셔너리에 있으면 제거하고 그 값을 돌려줌. 없으면 default 반환.

  default가 없는 상태에서 해당 key가 딕셔너리에 없는 경우 `KeyError` 발생

- `.update([other])` : other가 제공하는 key, value 쌍으로 딕셔너리를 덮어씀

  ```python
  my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
  my_dict.update(apple='사과아')
  print(my_dict)
  ------------------------------------------------------------
  {'apple': '사과아', 'banana': '바나나', 'melon': '멜론'}
  
  # update 할 때, key에 따옴표 x
  ```





---

## 얕은 복사와 깊은 복사

### immutable 데이터

```
얕은 복사를 해도 원래의 값이 바뀌지 않음
```





### mutable 데이터

- 변수만 복사하면 바라보는 객체가 동일하기 때문에 나머지도 수정되는 현상 발생

```python
original_list = [1, 2, 3]
copy_list = original_list
copy_list[0] = 5
print(original_list)
-------------------------------
[5, 2, 3]
```





#### 얕은 복사(Shallow copy)

> 2차원 리스트와 같이 mutable 객체 안에 mutable 객체가 있는 경우 문제가 됨

- slice 연산자 사용 `[:]` : 슬라이싱하여 할당 시, 새로운 id가 부여되며 서로 영향 x
- `list()` 활용 : 리스트로 한번 더 형변환을 해주어 할당





#### 깊은 복사(Deep copy)

> 새로운 객체를 만들고 원복 객체 내에 있는 객체에 대한 복사를 재귀적으로 삽입

```python
import copy

a = [1, 2, [1, 2]]
b = copy.deepcopy(a)

b[2][0] = 3
print(a)
print(b)
--------------------------------------
[1, 2, [1, 2]]
[1, 2, [3, 2]]
```

