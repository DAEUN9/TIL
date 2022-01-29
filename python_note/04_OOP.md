# OOP

### 객체(Object)

> 모든 객체는 타입, 속성, 조작법을 가짐

### 객체 중심의 장점

- 코드의 직관성
- 활용의 용이성
- 변경의 유연성





### 기본 문법

```python
# 클래스 정의
class MyClass:
    pass

# 인스턴스 생성
my_instance = MyClass()

# 속성 접근
my_instance.my_attribute

# 메서드 호출
my_instance.my_method()
```





### 인스턴스(instance)

> 정의된 클래스에 속하는 객체를 해당 클래스의 인스턴스라고 함

```python
- 인스턴스 변수: 인스턴스의 속성, 생성자 메서드에서 self.변수명 로 정의
				인스턴스가 생성된 이후 인스턴스.변수명 로 접근 및 할당
				# 활용법
				class Person:
                    pass

                p1 = Person()
                p1.name = 'jack'	# 인스턴스 변수
                p1.age = 25		# 인스턴스 변수
                
- 인스턴스 메서드: 메서드 호출시, 첫번째 인자로 인스턴스 자기자신에 해당하는 self 전달
				# 활용법
				class MyClass:
                        def instance_method(self, arg1, arg2, ...):
                            ...

                    my_instance = MyClass()
                    my_instance.instance_method(.., ..)

- 생성자(constructor) 메서드: 인스턴스 객체가 생성될 때 자동으로 호출
							반드시 __init__ 이라는 이름으로 정의
							# 활용법
							class MyClass:
                            def __init__(self):
                                print('생성될 때 자동으로 호출되는 메서드입니다.')
                             # 인스턴스 속성 정의 가능
                      
- 소멸자(destructor) 메서드: 인스턴스 객체가 소멸(파괴)되기 직전에 자동으로 호출
							반드시 __del__ 이라는 이름으로 정의
							# 활용법
							def __del__(self):
    							print('소멸될 때 자동으로 호출되는 메서드입니다.')
							del 인스턴스
```





### 속성(Attribute)

> 특정 데이터 타입(또는 클래스)의 객체들이 가지게 될 상태/데이터
>
> `self.<속성명> = <값>` 혹은 `<인스턴스>.<속성명> = <값>` 으로 설정





### 매직(스페셜) 메서드

> 더블언더스코어(`__`) 가 있고 특별한 일을 하기 위해 만들어진 메서드

```python
'__str__(self)',
'__len__(self)',
'__repr__(self)',
'__lt__(self, other)',
'__le__(self, other)',
'__eq__(self, other)',
'__ne__(self, other)',
'__gt__(self, other)',
'__ge__(self, other)',
```

- `__str__(self)` : 특정 객체(인스턴스)를 출력(`print()`) 할 때 보여줄 내용 정의

- `__gt__(self, other)` : 특정 객체(인스턴스)간 대/소 비교 연산에 사용

- `__gt__(self, other)` : 특정 객체(인스턴스)가 같은지 비교

  ```python
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      def __gt__(self, other):
          return self.age > other.age
      def __eq__(self, other):
          return self.age == other.age
  
  p1 = Person('1', 1)
  p2 = Person('2', 2)
  p3 = Person('3', 1)
  
  print(p1 > p2)
  print(p1 == p3)
  ----------------------------------------------------
  False
  True
  ```





### 클래스(class)

> 객체들의 분류를 정의할 때 사용
>
> `클래스 이름` 은 `PascalCase` 로 정의

```python
# 활용법
class <클래스이름>:
    <statement>
class ClassName:
    statement
    
- 클래스 변수: 모든 인스턴스가 공유, 클래스.변수명 으로 접근 및 할당
            # 활용법
            class Circle:
            	pi = 3.14
                
- 클래스 메서드: @classmethod 데코레이터 사용, 호출시 첫 번째 인자로 cls(클래스) 전달
    			# 활용법
        		class MyClass:
                    @classmethod
                    def class_method(cls, arg1, arg2, ...):
                        ...
                # 자동으로 첫 번째 인자로 클래스(MyClass)가 들어갑니다.
                MyClass.class_method(.., ..)
                
- 스태틱 메서드: @staticmethod 데코레이터 사용, 인스턴스와 클래스의 속성과 무관한 메서드
    			호출시, 어떤 인자도 전달되지 않음
        		속성을 다루지 않고 단지 기능(행동)만을 하는 메서드 정의할 때 사용
            	# 활용법
                class MyClass:
                    @staticmethod
                    def static_method(arg1, arg2, ...):		#self나 cls 안받음
                        ...
                MyClass.static_method(.., ..)	
```





### 인스턴스와 클래스 간의 이름 공간

> 인스턴스에서 특정 속성에 접근하면, 인스턴스 - 클래스 순으로 탐색
>
> 인스턴스에서 클래스 메서드와 스태틱 메서드는 호출하지 않는다.





---

## OOP의 핵심 개념

- 추상화 (Abstraction)
- 상속 (Inheritance)
- 다형성 (Polymorphism)
- 캡슐화 (Encapsulation)





### 추상화(Abstraction)

- 세부적인 내용은 감추고 필수적인 부분만 표현
- 여러 클래스가 공통적으로 사용할 속성 및 메서드를 추출하여 기본 클래스로 작성
  - professor와 student의 공통 속성과 메서드를 추출하여 person으로 추상화





### 상속(Inheritance)

- 클래스의 모든 속성을 자식 클래스에게 상속
- 재사용성이 높아짐

```python
# 활용법
class ChildClass(ParentClass):
    <code block>
```

- `issubclass(class, classinfo)`: class가 classinfo의 subclass인 경우 `True` 반환

- `isinstance(object, classinfo)`: object가 classinfo의 인스턴스거나 subclass인 경우 `True` 반환

  ```python
  issubclass(Student, Person)
  isinstance(s1, Person)
  ------------------------------
  True
  True
  
  # 내장 자료형들도 상속 관계가 있다. ex) bool, int
  ```

- `super()`: 부모 클래스의 내용을 사용가능

  ```python
  # 활용법
  class ChildClass(ParentClass):
      def method(self, arg):
          super().method(arg) 
  ```





### 다형성(Polymorphism)

- 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 각기 다른 방식으로 응답 가능

  #### 메서드 오버라이딩

  > 자식 클래스에서 부모 클래스의 메서드 재정의





### 캡슐화(Encapsulation)

- 객체 일부 구현 내용에 대해 외부로부터의 직접적인 액세스 차단

- 파이썬에서 암묵적으로 존재, 언어적으로는 존재x

  ```
  # 접근제어자의 종류
  - Public Access Modifier
  - Protected Access Modifier
  - Private Access Modifier
  ```

  #### public Member

  > 언더바 없이 시작하는 메서드나 속성들. 어디서나 호출가능
  >
  > 하위 클래스에서 메서드 오버라이딩을 허용

  #### Protected Member

  > 언더바 1개로 시작하는 메서드나 속성들. 부모 클래스 내부와 자식 클래스에서만 호출가능
  >
  > 하위 클래스에서 메서드 오버라이딩 허용

  #### Private Member

  > 언더바 2개로 시작하는 메서드나 속성들. 본 클래스 내부에서만 사용
  >
  > 하위 클래스 상속 및 호출 불가능
  >
  > 외부 호출 불가능

  ```python
  class Person:    
      def __init__(self, name, age):
          self.name = name
          self.__age = age
          
      def get_age(self): 
          return self.__age
  ```

  



#### `getter` 메서드와 `setter` 메서드

- 변수의 접근할 수 있는 메서드를 별도로 생성 가능

```python
- getter 메서드: 변수의 값을 읽는 메서드
				@property 데코레이터를 사용
- setter 메서드: 변수의 값을 설정하는 성격의 메서드
				@변수.setter를 사용
				
                # 예시
                class Person:

                    def __init__(self, age):
                        self._age = age 

                    @property	# 값을 읽어옴
                    def age(self):
                        return self._age

                    @age.setter		# 값을 설정 
                    def age(self, new_age):
                        if new_age <= 19:
                            raise ValueError('Too Young For SSAFY')
                            return

                        self._age = new_age
                p1.age = 19
                print(p1.age)
                --------------------------------------
                ValueError: Too Young For SSAFY
```





#### 다중 상속

- 두개 이상의 클래스를 상속
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정





#### 상속관계에서의 이름 공간과 MRO(Method Resolution Order)

- 기존의 `인스턴스 -> 클래스` 순으로 이름 공간을 탐색해나가는 과정에서 상속이 있으면 아래와 같이 확장

  - 인스턴스 -> 자식 클래스 - > 부모 클래스

- MRO는 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인

  ```python
  # 활용법
  ClassName.__mro__
  
  # 또는
  ClassName.mro()
  ```





