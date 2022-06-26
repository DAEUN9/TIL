# 람다와 스트림

### 람다식

- 익명함수 라고도 함
- 메서드를 하나의 식으로 표현



### 람다식 작성하기

- 메서드에서 이름과 반환타입을 제거하고
- 매개변수 선언부와 몸통{} 사이에 `->`를 추가하기만 하면 된다.
- 반환값이 있는 메서드인 경우, return문 대신 식으로 대신 가능
  - 문장이 아닌 식이므로 끝에 `;`를 붙이지 x
- 매개변수 타입이 추론가능한 경우 생략가능
- 괄호 안의 문장이 return문일 경우 괄호 생략 불가

```java
(int a, int b) -> { return a > b ? a : b; }	// OK
(int a, int b) -> return a > b ? a : b	// 에러
```



### 람다식은 익명 함수? 익명 객체!

```java
타입 f = (int a, int b) -> a > b ? a : b;	// 참조변수의 타입을 뭘로 해야 할까?
// 클래스 또는 인터페이스가 가능
// 람다식과 동등한 메서드가 정의되어 있는 것이어야 함
```



### 함수형 인터페이스

- 람다식을 다루기 위한 인터페이스
- 함수형 인터페이스는 하나의 추상메서드만 정의되어야 함

```java
@FunctionalInterface
interface MyFunction {	// 함수형 인터페이스 MyFunction을 정의
    public abstract int max(int a, int b);
}
```



### 함수형 인터페이스 타입의 매개변수, 반환 타입

- 참조변수 없이 직접 람다식을 매개변수로 지정도 가능

```java
aMethod(() -> System.out.println("myMethod()"));	// 람다식을 매개변수로 지정
```

- 메서드 반환타입이 함수형 인터페이스라면
  - 추상메서드와 동등한 람다식을 가리키는 참조변수 반환가능
  - 람다식을 직접 반환가능

```java
MyFunction myMethod() {
    MyFunction f = ()->{};
    return f;			// 이 줄과 윗 줄을 한줄로 줄이면, return ()->{};
}
```



### java.util.function 패키지📚

- 자주 쓰이는 형식의 메서드를 함수형 인터페이스로 미리 정의



### Predicate의 결합

- and(), or(), negate()로 연결
- 람다식을 직접 넣어도 됨

```java
Prediate<Integer> all = notP.and(i -> i < 200).or(i -> i%2 == 0);
```

- static메서드인 isEqual()은 두 대상을 비교하는 Predicate를 만들 때 사용
- 또 다른 비교대상은 test()의 매개변수로 지정

```java
// str1과 str2가 같은지 비교
boolean result = Predicate.isEqual(str1).test(str2);
```



### 컬렉션 프레임웍과 함수형 인터페이스

- 컬렉션 프레임웍의 인터페이스의 디폴트 메서드 일부는 함수형 인터페이스 사용



### 메서드 참조

- 람다식이 하나의 메서드만 호출하는 경우 람다식 간단히 가능
  - `클래스이름::메서드이름` 또는 `참조변수::메서드이름`

```java
// 예시
Function<String, Integer> f = (String s) -> Integer.parseInt(s);
```

```java
Function<String, Integer> f = Integer::parseInt;	// 메서드 참조
```

| 종류                          | 람다                       | 메서드 참조       |
| ----------------------------- | -------------------------- | ----------------- |
| static메서드 참조             | (x) -> ClassName.method(x) | ClassName::method |
| 인스턴스메서드 참조           | (obj, x) -> obj.method(x)  | ClassName::method |
| 특정 객체 인스턴스메서드 참조 | (x) -> obj.method(x)       | obj:method        |



### 생성자의 메서드 참조

- 필요하다면 함수형 인터페이스 새로 정의

- 메서드 참조는 람다식을 마치 static변수처럼 다룰 수 있게 해줌

- 배열을 생성할 때

  ```java
  Function<Integer, int[]> f = x -> new int[x];	// 람다식
  Function<Integer, int[]> f2 = int[]::new;	// 메서드 참조
  ```

  

### 스트림

- 데이터 소스 추상화
- 데이터를 다루는데 자주 사용되는 메서드를 정의
- 배열이나 컬렉션뿐만 아니라 파일에 저장된 데이터도 모두 같은 방식으로 다룰 수 있음

```java
String[]	strArr = {"aaa", "ddd", "ccc"};
List<String> strList = Arrays.asList(strArr);

// 스트림 생성
Stream<String> strStream1 = strList.stream();
Stream<String> strStream2 = Arrays.stream(strArr);

// 두 스트림으로 데이터 소스의 데이터를 읽어서 정렬하고 화면에 출력
strStream1.sorted().forEach(System.out::println);
strStream2.sorted().forEach(System.out::println);
```



### 스트림의 특징

- 스트림은 데이터 소스를 변경하지 않는다
- 스트림은 일회용
- 스트림은 작업을 내부 반복으로 처리

```java
for(String str : strList)
    System.out.println(str);

// 같음
stream.forEach(System.out::println);
```

- 지연된 연산
  - 중간연산 x
- Stream<Integer>와 IntStream
- 병렬 스트림
  - parallel(): 병렬 연산 지시
  - sequential(): 병렬로 처리되지 않게 함



### 스트림 만들기 - 컬렉션

- stream()은 해당 컬렉션을 소스로 하는 스트림을 반환

```java
Stream<E> stream()	// Collection인터페이스의 메서드
```



### 스트림 만들기 - 배열

```java
// 문자열 스트림
Stream<String> strStream=Stream.of("a","b","c"); // 가변 인자
Stream<String> strStream=Stream.of(new String[]{"a","b","c"});
Stream<String> strStream=Arrays.stream(new String[]{"a","b","c"});
Stream<String> strStream=Arrays.stream(new String[]{"a","b","c"}, 0, 3);

// 기본형 배열 소스 스트림
IntStream IntStream.of(int... values)	// Stream이 아니라 IntStream
```



### 스트림 만들기 - 임의의 수

```java
IntStream intStream = new Random().ints();	// 무한 스트림
intStream.limit(5).forEach(System.out::println);	// 5개의 요소만 출력
IntStream intStream = new Random().ints(5);	// 크기가 5인 난수 스트림
```



### 스트림 만들기 - 특정 범위의 정수

```java
IntStream IntStream.range(int begin, int end)
IntStream IntStream.rangeClosed(int begin, int end)
```



### 스트림 만들기 - 람다식 iterate(), generate()

- 계산되는 값들을 요소로 하는 무한 스트림을 생성

``` java
static <T> Stream<T> iterate(T seed, UnaryOperator<T> f)
static <T> Stream<T> generate(Supplier<T> s)
```

- iterate(): 지정값부터 람다식 결과를 다시 seed값으로 계산 반복

- generate(): 람다식에 의해 계산되는 값을 요소로 무한 스트림 생성

  - 이전 결과를 이용해서 다음 요소를 계산 x
  - 정의된 매개변수 타입은 Supplier<T>이므로 매개변수 없는 람다식만 허용
  - 기본형 스트림 타입의 참조변수로 다루기 불가능

  ```java
  // 에러
  IntStream evenStream = Stream.iterate(0, n->n+2);
  DoubleStream randomStream = Stream.generate(Math::random);
  
  // 메서드로 변환
  IntStream evenStream = Stream.iterate(0, n->n+2).mapToInt(Integer::valueOf);
  Stream<Integer> stream = evenStream.boxed(); // IntStream -> Stream<Integer>
  ```

  

### 스트림 만들기 - 파일과 빈 스트림

- list()는 지정된 디렉토리에 있는 파일의 목록을 소스로 하는 스트림을 생성해서 반환

```java
Stream<Path> Files.list(Path dir)
```

- 빈 스트림

```java
Stream emptyStream = Stream.empty();
```



### 스트림의 연산

- 중간 연산: 연산 결과가 스트림인 연산. 스트림에 연속해서 중간 연산가능
- 최종 연산: 연산 결과가 스트림이 아닌 연산. 스트림의 요소를 소모하므로 단 한번만 가능



### 스트림의 중간연산 - skip(), limit()

- 스트림을 잘라낼때 사용

```java
Stream<T> skip(long n)
Stream<T> limit(long maxSize)
```



### 스트림의 중간연산 - filter(), distinct()

```java
Stream<T> filter(Predicate<? super T> predicate)
Stream<T> distinct()
```



### 스트림의 중간연산 - sorted()

```java
Stream<T> sorted()
Stream<T> sorted(Comparator<? super T> comparator)
```



### 스트림의 중간연산 - Comparator의 메서드

- 정렬
- 가장 기본적인 메서드는 comparing()



### 스트림의 중간연산 - map()

- 원하는 필드만 뽑아내거나 특정형태로 변환
- 매개변수로 T타입을 R타입으로 변환해서 반환하는 함수 지정

```java
Stream<R> map(Function<? super T,? extends R> mapper)
```



### 스트림의 중간연산 - peek()

- 처리 확인
- 스트림 요소를 소모하지 않으므로 연산 사이에 여러 번 끼워 넣어도 됨



### 스트림의 중간연산 - flatMap()

- 스트림 타입이 Stream<T[]>인 경우, Stream<T>로 변환

```java
// map()과 flatMap()차이

// map(Arrays::stream)
Stream<String[]>
    ->
Stream<Stream<String>>
    
// flatMap(Arrays::stream)
Stream<String[]>
    ->
Stream<String>
```



### Optional<T>

- T타입의 객체를 감싸는 래퍼클래스
- 모든 타입의 객체를 담을 수 있다

```java
public final class optional<T> {
    private final  T value;	// T타입의 참조변수
    ...
}
```

- null체크 안하고 간단히 처리가능



### Optional<T>객체 생성하기

- of() 또는 ofNullable()을 사용한다
  - null 가능성 있다면 ofNullable()
- 기본값 초기화는 empty()



### Optional<T>객체의 값 가져오기

- get()사용
- null이면 에러발생하여 orElse()로 대체값 지정 가능
- 대체값 반환 람다식 지정가능
  - orElseGet()
  - orElseThrow()
- isPresent(): null이면 false, 아니면 true
- ifPresent(Consumer<T> block)은 값이 있으면 람다식 실행, 없으면 아무일 x



### 스트림의 최종연산 - forEach()

```java
void forEach(Consumer<? super T> action)
```



### 스트림의 최종연산 - 조건검사

```java
boolean allMatch (Predicate<? super T> predicate) // 모든 요소가 일치하면 참
boolean anyMatch (Predicate<? super T> predicate) // 하나의 요소라도 일치하면 참
boolean noneMatch(Predicate<? super T> predicate) // 모든 요소가 불일치하면 참
```

```java
Optional<T> findFirst()	// 조건에 일치하는 첫 번째 요소 반환
Optional<T> findAny()	// 조건에 일치하지 않는 요소를 하나 반환(병렬 스트림)
```



### 스트림의 최종연산 - reduce()

- 스트림의 요소를 줄여나가면서 연산 수행, 최종결과 반환

```java
Optional<T> reduce(BinaryOperator<T> accumulator)
```



### 스트림의 최종연산 - reduce()의 이해

- 초기값과, 어떤 연산으로 스트림의 요소를 줄여나갈지 결정필요



### collect()와 Collectors

- collect(): 스트림의 최종연산, 매개변수로 컬렉터를 필요로함
- Collector: 인터페이스, 컬렉터는 이 인터페이스를 구현해야 함
- Collectors: 클래스, static메서드로 미리 작성된 컬렉터 제공



### 스트림의 통계 - counting(), summingInt()

- summingInt()와 summarizingInt() 혼동 주의



### 스트림을 리듀싱 - reducing()

- Collector reducing() 3종

```java
Collector reducing(BinaryOperator<T> op)
Collector reducing(T identity, BinaryOperator<T> op)
Collector reducing(U identity, Function<T,U> mapper, BinaryOperator<U> op)
```



### 스트림을 문자열로 결합 - joining()

- 모든 요소를 하나의 문자열로 연결해서 반환
- 요소가 문자열이 아니면 map()으로 문자열 변환 먼저해야 함



### 스트림의 그룹화와 분할

- groupingBy(): 스트림 요소 -> Function 분류
- partioningBy(): 스트림 요소 -> Predicate로 분류



### 스트림의 분할 - partioningBy()



### 스트림의 그룹화 - groupingBy()



### 스트림의 변환📚



