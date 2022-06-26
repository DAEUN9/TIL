# 지네릭스(Generics)

- 메서드나 컬렉션 클래스에 컴파일 시의 타입체크
- 장점
  - 타입 안정성 제공
  - 타입체크와 형변환을 생략할 수 있으므로 코드가 간결해짐

```java
// 제네릭스 적용 X
ArrayList tvList = new ArrayList();

tvList.add(new Tv());
Tv t = (Tv)tvList.get(0);

// 제네릭스 적용 O
ArrayList<Tv> tvList = new ArrayList<Tv>();
tvList.add(new Tv());
Tv t = tvList.get(0);	// 형변환 불필요
```



### 타입 변수

- `<>`안에 있는 E를 타입변수라고 함
  - 일반적으로 Type의 첫 글자 따서 T
- Map<K, V>

- 타입 변수에 대입

```java
// 제네릭스 X
public class ArrayList<E> extends AbstractList<E> {	// 일부 생략
    private transient E[] elementData;
    public boolean add(E o) { /* 내용생략 */ }
    public E get(int index) { /* 내용생략 */ }
    ...
}

// 타입 변수 E 대신에 실제 타입 Tv 대입
ArrayList<Tv> tvList = new ArrayList<Tv>();

// 타입변수 E가 지정 타입으로 바뀜
public class ArrayList extends AbstractList<E> {	// 일부 생략
    private transient Tv[] elementData;
    public boolean add(Tv o) { /* 내용생략 */ }
    public Tv get(int index) { /* 내용생략 */ }
    ...
}
```



### 지네릭스의 용어

- `class Box<T> {}`
  - `Box<T>`: 지네릭 클래스, T의 Box 또는 T Box라고 읽음
  - `T`: 타입 변수 또는 타입 매개변수
  - `Box`: 원시타입
- 컴파일 후에 Box<T>는 원시타입 Box로 바뀜(지네릭 타입 제거)



### 지네릭 타입과 다형성

- 객체 생성시에 참조변수의 지네릭 타입과 생성자의 지네릭 타입 같아야 함

- 클래스 타입 간의 다형성 적용 가능

```java
List<Tv> list = new ArrayList<Tv>();	// OK. 다형성. ArrayList가 List를 구현
List<Tv> list = new LinkedList<Tv>();	// Ok. 다형성. LinkedList가 List를 구현
```

- ArrayList에 Product의 자손 객체만 저장

```java
ArrayList<Product> list = newArrayList<Product>();
list.add(new Product());
list.add(new Tv());
list.add(new Audio());

// 저장된 객체 꺼낼 때, 형변환 필요
Product P = list.get(0);	// Product객체는 형변환 필요없음
Tv t = (Tv)list.get(1);		// Product의 자손객체들은 형변환을 필요
```



### 제한된 지네릭 클래스

- 지네릭 타입에 extends를 사용하면 특정 타입의 자손들만 대입할 수 있게 제한
- 인터페이스도 extends사용
  - implements사용하지 않는다는 점 주의
  - 여러개 &기호로 연결



### 와일드 카드

- `<? extends T>`: 와일드 카드의 상한 제한. T와 그 자손들만 가능
- `<? super T>`: 와일드 카드의 하한 제한. T와 그 조상들만 가능
- `<?>`: 제한 x



### 지네릭 메서드

- `static <T> void sort(List<T> list, Comparator<? super T> c)`
- 지네릭 타입 매개변수와 지네릭 메서드 매개변수 별개
- 지네릭 메서드 내의 타입은 지역적으로 사용
- 클래스 이름 생략 불가



### 지네릭 타입의 형변환

- 지네릭 타입과 원시 타입간의 형변환 가능
- 대입된 타입이 다른 지네릭 타입 간에는 형변환 불가능

```java
Box<Object> objBox = null;
Box<String> strBox = null;

objBox = (Box<Object>)strBox; // 에러
strBox = (Box<String>)objBox; // 에러

Box<? extends Object> wBox = new Box<String>();	// Ok
```



### 열거형(enum)

- 여러개 선언

```java
class Card {
    enum Kind { COVER, HEART, DIAMONT, SPADE }
    enum Value { TWO, THREE, FOUR}
    
    final Kind kind;
    final Value value;
}
```

- 열거형에 정의된 상수 사용: `열거형이름.상수명`



### 열거형의 조상 - java.Iang.Enum

| 메서드                                    | 설명                                               |
| ----------------------------------------- | -------------------------------------------------- |
| Class<E> getDeclaringClass()              | 열거형의 Class객체를 반환                          |
| String name()                             | 열거형 상수의 이름을 문자열로 반환                 |
| int ordinal()                             | 열거형 상수가 정의된 순서 반환(0시작)              |
| T valueOf(Class<T> enumType, String name) | 저장된 열거형에서 name과 일치하는 열거형 상수 반환 |

- 자동 추가 메서드
  - `values()`: 열거형에 정의된 모든 상수 출력
  - `valueOf(type name)`: 열거형 상수의 이름으로 문자열 상수에 대한 참조 얻기



### 열거형에 멤버 추가

- 상수값이 불규칙하면 열거형 상수 이름 옆에 원하는 값을 괄호와 함께 적음
- 저장할 수 있는 인스턴스 변수와 생성자 새로 추가해야함
- 열거형의 생성자는 외부에서 호출불가
- 열거형의 생성자는 제어자가 묵시적으로 private

```java
enum Direction {
    EAST(1), SOUTH(5), WEST(-1), NORTH(10);	// 끝에 ';'를 추가해야함
    
    private final int value;	// 정수를 저장할 필드(인스턴스 변수)
    Direction(int value){ this.value = value;} // 생성자
    
    public int getValue() { return value; }
}
```



### 애너테이션

- 프로그램의 소스코드 안에 다른 프로그램을 위한 정보를 미리 약속된 형식으로 포함

- 주석처럼 존재



### @Override

- 조상의 메서드를 오버라이딩하는 것임을 알림
- 같은 이름 메서드 조상에 없으면 에러메시지



### @Deprecated

- 더이상 사용하지 않을것을 권함
- 다른것으로 대체되었다는 의미



### @Functionallnterface

- 함수형 인터페이스 선언
  - 함수형 인터페이스는 추상메서드가 하나뿐이어야 한다는 제약이 있음



### @SuppressWarnings

- 경고메시지가 나타나지 않게 억제
- 둘 이상 경고 동시에 억제
  - `@SuppressWarinings({ "deprecation", "unchecked", "varags" })`



### 메타 애너테이션

> 애너테이션을 위한 애너테이션



### @Target

- 애너테이션이 적용가능한 대상 지정



### @Retention

- 애너테이션이 유지되는 기간 지정



### @Documented

- 애너테이션에 대한 정보가 javadoc으로 작성한 문서에 포함되도록 함



### @Inherited

- 애너테이션이 자손 클래스에 상속되도록 함



### @Repeatable

- 여러번 반복해서 붙일 수 있음
- 이 애너테이션들을 하나로 묶어서 다룰 수 있는 애너테이션 추가정의 필요



### 애너테이션 타입 정의하기

```java
@interface 애너테이션이름 {
    타입 요소이름();	// 애너테이션의 요소 선언
    	...
}
```

- 애너테이션 요소: 반환값 O, 매개변수 X, 추상 메서드 형태
  - 상속통해 구현 안해도됨
- 기본값이 있는 요소는 애너테이션을 적용 할 때 지정하지 않으면 기본값 사용



### 모든 애너테이션의 조상

- 모든 애너테이션의 조상은 Annotation
- 상속이 허용되지 않으므로 명시적으로 Annotation을 조상으로 지정 X



### 마커 애너테이션

- 요소가 하나도 정의되지 않은 애너테이션



### 애너테이션 요소의 규칙

- 요소 타입은 기본형, String, enum, 애너테이션, Class만 허용
- () 안에 매개변수를 선언할 수 없다.
- 예외를 선언할 수 없다.
- 요소를 타입 매개변수로 정의할 수 없음

