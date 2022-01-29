# 제어문

### 조건 표현식(Conditional Expression)

- 삼항 연산자(ternary Operator)라고 부르기도 한다.

```python
# 활용법
	true_value if <조건식> else false_value
```





### 딕셔너리 순회(반복문 활용)

```
딕셔너리를 순회하면 key를 반환하고 key를 이용해 value에도 접근 가능
```





### enumerate()

- 인덱스(index)와 값(value)을 함께 활용 가능

```python
# 예시
	for idx, member in enumerate(members, start=1)
		print(idx, member)
	------------------------------
	1 민수
	2 영희
튜플임
```





### List Comprehension

```python
# 활용법
	[expression for 변수 in iterable]
	list(expression for 변수 in iterable)
# 예시
	a= [[i, j] for i in range(5) for j in range(3)]
	print(a)
	-----------------------------------
	[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2]]
```





### Dictionary comprehension

```python
# 활용법
	{키: 값 for 요소 in iterable}
	dict({키: 값 for 요소 in iterable})
# 예시
	cubic = {number:number**3 for number in range(1,4)}
	print(cubic)
	----------------------------------
	{1: 1, 2: 8, 3: 27}
```





### for - else

- for문을 break없이 빠져나온 경우 else문 실행(for문을 전부 수행)

```python
# 예시
	for i in numbers:
    if i == 4:
        print('True')
        break
    else:
        print('False')
   -------------------------
   False
```

