# 객체 지향 프로그래밍1

#### 1. Type Class

python에 기본적으로 저장되어 있는 클래스

```
complex, str, list, dict, int, type, ...
```

#### 2. Magic Method

매직 메서드의 역할

```
`__init__` : 생성자. 인스턴스 객체가 생성될때 자동 호출
`__del__` : 소멸자. 인스턴스 객체가 소멸되기 직전에 자동 호출
`__str__` : 특정 객체를 출력할 때 문자열로 출력 (print 함수) 호출시 출력문자
`__repr__` : 특정 객체를 출력할 때 문자열로 출력 (개발자에게 필요한 객체정보를 출력)
```

#### 3. Instance Method

문자열, 리스트, 딕셔너리 등을 조작하는 메서드

```
`.append()` : 리스트의 맨 뒤에 원소 추가
`.index()` : 값의 인덱스 값을 반환
`.insert()`: 특정 위치에 값을 삽입
```

#### 4. Module Import

fino.py 파일에서 fibo_recursion함수 recursion으로 불러오기

```python
from fibo import fibo_recursion as recursion

recursion(4)
```

----

# 객체 지향 프로그래밍2

#### 1. pip

`$ pip install faker` 명령어 

(1) 무엇을 위한 명령인지

(2) 실행은 어디에서 해야하는지

```
(1) 패키지 Faker를 설치하기 위한 명령어
(2) bash, cmd 환경
```

### 2. Basic Usages

아래 코드의 라인별 의미

```python
from faker import Faker
fake = Faker()
fake.name()
```

```
# 1 faker 패키지에서 Faker 클래스 를 끌어와 사용하기 위한 코드이다.
# 2 Faker는 클래스, faker는 인스턴스 이다
# 3 name()은 fake의 메서드 이다.
```

### 3. Localization

직접 해당하는 기능 구현

(1) 인자 없이 호출 시에는 영문이 기본 설정이다. (en_US)

(2) Locale 정보를 포함하여 호출 시에는 해당 언어 설정을 따른다.

```python
class Faker():
    
    def __(a)__((b),(c)):
        pass
```

```
(a) init
(b) self
(c) Locale = 'en_US'
```

### 4. Seeding the Generator

출력되는 결과, seed()는 어떤 종류의 메서드인지

```python
fake = Faker('ko_KR')
Faker.seed(4321)

print(fake.name())		# 1

fake2 = Faker('ko_KR')
print(fake2.name())		# 2
```

```
# 1 : 이도윤
# 2 : 이지후
---------------------
`seed()` : 클래스 메서드
```

### 4. Seeding the Generator

출력되는 결과, seed_instance()는 어떤 종류의 메서드인지, seed()와 seed_instance()는 각각 어떠한 용도

```python
fake = Faker('ko_KR')
Faker.seed_instance(4321)

print(fake.name())		# 1

fake2 = Faker('ko_KR')
print(fake2.name())		# 2
```

```
# 1 : 이도윤
# 2 : 김유진
------------------
`seed_instance()` : 인스턴스 메서드
------------------
seed()는 시작값을 설정하고 클래스의 모든 객체에 영향을 끼친다.
seed_instance()는 seed()와 같은 기능을 하지만 인스턴스 내부에서만 영향을 미침
```

---

# 객체 지향 프로그래밍3

#### 1. Circle 인스턴스 만들기

반지름이 3이고 x,y좌표가 (2,4)인 Circle 인스턴스를 만들어
넓이와 둘레 출력

```python
class Circle:
    pi = 3.14

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.pi * self.r * self.r

    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)


c = Circle(3, 2, 4)
print(c.area())
print(c.circumference())
```

#### 2. Dog와 Bird는 Animal이다

Animal 클래스를 상속 받아 동작하는 Dog 클래스와 Bird 클래스를 작성

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def fly(self):
        print(f'{self.name}! 푸드덕!')

dog = Dog('멍멍이')
dog.walk()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()
```

#### 3. 오류의 종류

제시된 오류들이 각각 어떠한 경우에 발생하는지 간단하게 작성

```
ZeroDivisionError: 0으로 나누려고 했을 때
NameError: 존재하지 않는 이름일 때
TypeError: 자료형이 올바르지 못한 경우
IndexError: 존재하지 않는 index로 조회할 경우
KeyError: 존재하지 않는 Key로 접근한 경우
ModuleNotFoundError: 존재하지 않는 Module을 import 하는 경우
ImportError: Module은 찾았으나 존재하지 않는 클래스/함수를 가져오는 경우
```

---

# 객체 지향 프로그래밍4

### .도형 만들기

 Python 클래스를 활용하여 점(Point)과 사각형(Rectangle)을 표현

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Rectangle(Point):
    def __init__(self, p1, p2):
        self.x1, self.y1 = p1.x, p1.y
        self.x2, self.y2 = p2.x, p2.y
        
    def get_area(self):
        h = self.y1 - self.y2
        w = self.x2 - self.x1
        return h * w

    def get_perimeter(self):
        h = self.y1 - self.y2
        w = self.x2 - self.x1
        return 2 * h + 2 * w

    def is_squre(self):
        h = self.y1 - self.y2
        w = self.x2 - self.x1
        if h == w:
            return True
        else:
            return False
```

```
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_squre())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)

print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_squre())
------------------------------------------
4
8
True
9
12
True
```

