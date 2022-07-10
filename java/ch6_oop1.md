### 객체지향 언어

- 코드의 재사용성이 높다
- 코드의 관리가 용이
- 신뢰성이 높은 프로그래밍



### 클래스와 객체

- 클래스: 객체를 정의해 놓은 것, 객체를 생성하는데 사용
- 객체(인스턴스: 실제로 존재하는 것
  - 속성(변수), 기능(메서드)



### 한 파일에 여러 클래스 작성하기

- public class가 있는 경우: 소스파일의 이름은 반드시 public class의 이름과 일치해야 함
- public class가 하나도 없는 경우: 소스파일의 이름은 아무 클래스의 이름
- public class가 둘 이상: 별도의 소스파일에 저장하거나 한 클래스의 public 떼야함



### 객체의 생성과 사용

```java
클래스명 변수명;
변수명 = new 클래스명();

Tv t;
t = new Tv();
```

- 인스턴스는 참조변수를 통해서만 다룰 수 있으며, 참조변수의 타입은 인스턴스의 타입과 일치해야 함



### 객체배열

- 참조변수들을 하나로 묶은 참조변수 배열
- 다뤄야할 객체의 수가 많을 때는 for문 사용

```java
Tv tv1, tv2, tv3;

// 같음
    
Tv[] tvArr = new Tv[3];

// 객체를 생성해서 배열의 각 요소에 저장
Tv[] tvArr = { new Tv(), new Tv(), new Tv() }
```



### 데이터와 함수의 결합

1. 변수: 하나의 데이터를 저장할 수 있는 공간
2. 배열: 같은 종류의 여러 데이터를 하나의 집합으로 저장할 수 있는 공간
3. 구조체: 서로 관련된 여러 데이터를 종류에 관계없이 하나의 집합으로 저장할 수 있는 공간
4. 클래스: 데이터와 함수의 결합(구조체 + 함수)



### 사용자 정의 타입

| 변수의 종류   | 선언위치                                                     | 생성시기                    |
| ------------- | ------------------------------------------------------------ | --------------------------- |
| 클래스 변수   | 클래스 영역                                                  | 클래스가 메모리에 올라갈 때 |
| 인스턴스 변수 | 클래스 영역                                                  | 인스턴스가 생성되었을 때    |
| 지역 변수     | 클래스 영역 이외의 영역<br />(메서드, 생성자, 초기화 블럭 내부) | 변수 선언문이 수행되었을 때 |

- 클래스 변수는 인스턴스 변수 앞에 static 붙이면 됨

- 인스턴스 변수는 인스턴스가 생성될 때 마다 생성되므로 인스턴스마다 각기 다른 값을 유지할 수 있지만, 클래스 변수는 모든 인스턴스가 하나의 저장공간을 공유하므로, 항상 공통된 값을 갖는다.



### 메서드란?

- 특정 작업을 수행하는 일련의 문장들을 하나로 묶음

```java
반환타입 메서드이름 (타입 변수명, 타입 변수명, ...)
{
    // 메서드 호출시 수행될 코드
}
```

- 반환값이 없는 경우 반환타입: `void`



### 호출스택

- 메서드가 호출되면 수행에 필요한 만큼의 메모리를 스택에 할당
- 메서드가 수행을 마치고나면 사용했던 메모리를 반환하고 스택에서 제거된다.
- 호출스택의 제일 위에 있는 메서드가 현재 실행 중인 메서드이다.
- 아래에 있는 메서드가 바로 위의 메서드를 호출한 메서드이다.



### 기본형 매개변수

- 기본형 매개변수 : 변수의 값을 읽기만 할 수 있음
- 참조형 매개변수 : 변수의 값을 읽고 변경



### static을 언제 붙여야 할까?

1. 클래스를 설계할 때, 멤버변수 중 모든 인스턴스에 공통으로 사용하는 것
2. 클래스 변수는 인스턴스를 생성하지 않아도 사용 가능
3. 클래스 메서드는 인스턴스 변수를 사용할 수 없다.
4. 메서드 내에서 인스턴스 변수를 사용하지 않는다면, static을 붙이는 것을 고려



### 메서드 간의 호출과 참조

- 클래스멤버가 인스턴스 멤버를 참조 또는 호출하고자 하는 경우에는 인스턴스를 생성
  - 단, 클래스멤버가 인스턴스 멤버를 참조 또는 호출하고자 하는 경우에는 인스턴스를 생성
- 클래스멤버가 존재하는 시점에 인스턴스 멤버가 존재하지 않을 수도 있음



### 오버로딩

- 한 클래스 내에 같은 이름의 메서드를 여러 개 정의
- 조건
  1. 메서드 이름이 같아야 함
  2. 매개변수의 개수 또는 타입이 달라야함
  3. 반환 타입은 관계없음



### 생성자

- 구조도 메서드와 유사하지만 리턴값이 없다.
- void를 사용하지 않고 아무것도 적지 않는다
- 조건
  1. 생성자의 이름은 클래스의 이름과 같아야 함
  2. 생성자는 리턴 값이 없음
- 메소드 오버로딩 가능



### 기본 생성자

- 컴파일 할 때, 소스파일 클래스에 생성자가 하나도 없으면 컴파일러나느 자동으로 기본 생성자르 ㄹ추가하여 컴파일

```java
클래스이름(){}	// 기본 생성자
Point(){}		// Point클래스의 기본 생성자
```



### 생성자에서 다른 생성자 호출하기 - this()

- 생성자의 이름으로 클래스이름 대신 this를 사용한다
- 한 생성자에서 다른 생성자를 호출할 때는 반드시 첫줄에서만 호출이 가능

```
this(매개변수)
```



### 객체 자신을 가리키는 참조변수 - this

- 인스턴스 변수 앞에 this 사용
  - 생성자의 매개변수로 정의된 지역변수로 서로 구별 가능



### 변수의 초기화

- 지역변수는 초기화 필수, 멤버변수는 선택
- 멤벼변수의 초기화
  - 클래스 변수 초기화 -> 인스턴스 변수 초기화
  - 자동 초기화 -> 명시적 초기화 -> 초기화 블럭, 생성자(복잡)
- 명시적 초기화: 변수를 선언과 동시에 초기화
- 초기화 블럭: 클래스 초기화 블럭, 인스턴스 초기화 블럭 두가지