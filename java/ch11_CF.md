# 컬렉션 프레임웍

### Collection인터페이스

- List와 Set의 조상
- 컬렉션 클래스에 저장된 데이터를 읽고, 추가하고 삭제



### List인터페이스

- 중복을 허용하면서 저장순서가 유지되는 컬렉션을 구현하는데 사용



### Set인터페이스

- 중복 X, 저장순서가 유지 X



### Map인터페이스

- 키 값을 하나의 쌍으로 묶어서 저장하는 컬렉션 클래스 구현
- 키는 중복 X, 값은 중복 가능



### ArrayList

- 저장순서 유지, 중복 허용
- 삭제
  1. 삭제할 데이터 아래로  칸씩 위로 복사하여 덮어씀
  2. 데이터가 모두 한 칸씩 이동하면 마지막 데이터 null로 변경
  3. size 1 감소



### Java API소스보기

- JDK설치한 디렉토리에서 src.zip압축 풀기
- 패키지별로 찾아 들어가 원하는 클래스의 실제소스를 볼 수 있음



### LinkedList

- 배열

  1. 크기 변경 X

     - 새로운 배열을 생성해 데이터를 복사해야함

     - 실행속도 향상을 위해서는 큰 배열을 생성해야 하므로 메모리 낭비

  2. 비순차적인 데이터의 추가 또는 삭제에 시간이 많이 걸림

     - 배열 중간에 데이터 추가하려면 다른 데이터들을 복사해서 이동

- LinkedList
  - 불연속적으로 존재하는 데이터를 서로 연결
  - 각 요소들은 자신과 연결된 다음 요소에대한 참조와 데이터로 구성 
  - 추가와 삭제 빠름



### ArrayList와 LinkedList의 비교

| 컬렉션     | 읽기(접근시간) | 추가/ 삭제 | 비 고                                                  |
| ---------- | -------------- | ---------- | ------------------------------------------------------ |
| ArrayList  | 빠르다         | 느리다     | 순차적인 추가삭제는 더 빠름<br />비효율적인 메모리사용 |
| LinkedList | 느리다         | 빠르다     | 데이터가 많을수록 접근성이 떨어짐                      |



### 스택과 큐

- 스택: ArrayList 컬렉션 클래스 적합
  - 순차적 데이터 삭제 추가
- 큐: LinkedList 컬렉션 클래스 적합
  - 첫번째 데이터의 추가 삭제



### Iterator, ListIterator, Enumeration

- Iterator: 컬렉션에 저장된 요소를 접근하는데 사용되는 인터페이스
- ListIterator: Iterator에 양방향 조회기능추가(List를 구현한 경우만 사용가능)
- Enumeration: Iterator의 구버전

```java
public interface Collection {
    ...
    public Iterator iterator();
    ...
}
```

- 재사용성 일관성 극대화

```java
List list = new ArrayList();	// 다른 컬렉션으로 변경할 때는 이 부분만 고침
Iterator it = list.iterator();

while(it.hasNext()) {	// boolean hasNext() 읽어올 요소가 있는지 확인
    System.out.println(it.next());	// Object next() 다음 요소를 읽어옴
}
```

- List클래스들은 Iterator대신 for문과 get()으로도 출력 가능



### Map과 Iterator

- 키 - 값 쌍
- Iterator() 바로 호출 불가 keySet()이나 entrySet()과 같은 메서드 통해 다시 Iterator()호출

```java
Map map = new Hashmap();
	...
Iterator it = map.entrySet().iterator();

// Iterator it = map.entrySet().iterator(); 는 아래 두 문장 합친 것
Set rDry = map.entrySet();
Iterator it = eSet.iterator();
```



### Arrays의 메서드 - 복사

- Arrays에 정의된 모든 메서드는 static메서드
- 배열의 복사
  - copyOf(): 배열 전체
    - `int[] arr2 = Arrays.copyOf(arr, 3)`
  - copyOfRange(): 배열 일부
    - `int[] arr3 = Arrays.copyOfRange(arr, 2, 4)`
    - 범위의 끝은 포함 x



### Arrays의 메서드 - 채우기, 정렬 검색

- 배열 채우기
  - fill(): 배열의 모든 요소 채우기
    - `Arrays.fill(arr, 9)`
  - setAll(): 배열을 채우는데 사용할 함수형 인터페이스를 매개변수로 받음
    - `Arrays.setAll(arr,(i) -> (int)(Math.random()*5)+1)`
- 배열의 정렬과 검색
  - sort(): 배열을 정렬
    - `Arrays.sort(arr)`
  - binarySearch(): 요소 index 반환
    - `Arrays.binarySearch(arr, 2)`



### Arrays의 메서드 - 비교와 출력

- 문자열의 출력
  - toString(): 일차원 배열 모든 요소 출력
  - deepToString(): 다차원 배열 모든 요소 출력
- 배열 비교
  - equals(): 두 배열 저장된 요소 boolean 반환
    - `Arrays.equals(str1, str2)`
  - deepEquals(): 다차원 배열 비교



### Arrays의 메서드 - 변환

- 배열을 List로 변환
  - asList(): 리스트 크기 변경 불가, 추가 삭제 불가
    - `Arrays.asList(1, 2, 3, 4)`
    - `Arrays.asList(new Integer[]{1, 2, 3, 4})`



### Comparator와 Comparable❗

- Comparable: 기본 정렬기준을 구현하는데 사용
  - 정렬가능
- Comparator: 기본 정렬기준 외에 다른 기준으로 정렬



### Integer와 Comparable

- Integer클래스의 compareTo()는 두 값 비교하여 같으면 0, 크면 -1, 작으면 1



### HashSet

- 중복된 요소 x
- 요소 추가는 add메서드나 addAll
  - 중복된 요소를 추가하고자 한다면 false
- 자정 순서를 유지하고자 한다면 `LinkedHashSet` 사용



### TreeSet

- 이진 탐색 트리의 성능을 향상시킨 '레드-블랙 트리'로 구현
- Object타입의 참조변수 하나와 두 개의 노드를 참조하기 위한 두 개의 참조변수 선언



### 이진 탐색 트리

- 중복 불가
- 검색과 정렬에 유리
- 노드의 추가 삭제에 시간이 오래걸림

- 저장 과정
  - 루트에 저장
  - 값의 크기를 비교하면서 트리를 따라 내려감



### HashMap과 Hashtable

- Entry라는 내부 클래스를 정의하고, 다시 Entry타입의 배열 선언

```java
// 비객체지향적인 코드
Object[] key;
Object[] value;

// 객체지향적인 코드
Entry[] table;

class Entry {
    Object key;
    Object value;
}
```



### Collections의 메서드 - 동기화

- 동기화가 필요할 때만 해당하는것 사용

```
static Collection synchronizedCollection(collection c)
static List synchronizedList(List list)
...
```



### Collections의 메서드 - 변경불가, 싱글톤

- 읽기전용

  ```java
  static Collection unmodifiableCollection(Collection c)
  static List unmodifiableList(List list)
      ...
  ```

- 싱글톤 컬렉션

  ```java
  static List singletonList(Object o)
  static Set singleton(Object o)	// singletonSet이 아님에 주의
  static Map singletonMap(Object key, Object value)
  ```

  

### Collections의 메서드 - 단일 컬렉션

- 한 종류의 객체만 저장 제한

  ```java
  static Collection checkedCollection(Collection c, Class type)
  static List checkedList(List list, Class type)
      ...
  ```

  

### 컬렉션 클래스 정리 & 요약

| 컬렉션                           | 특 징                                                        |
| -------------------------------- | ------------------------------------------------------------ |
| ArrayList                        | 배열 기반, 순차적인 추가삭제 제일 빠름, 임의의 요소에 대한 접근성 뛰어남 |
| LinkedList                       | 연결기반, 데이터의 추가 삭제 유리, 임의의 요소에 대한 접근성 좋지 않음 |
| HashMap                          | 배열과 연결이 결합된 상태<br />추가, 삭제, 검색, 접근성 모두 뛰어남<br />검색에는 최고의 성능 |
| TreeMap                          | 연결기반, 정렬과 검색에 적합<br />검색성능은 HashMap보다 떨어짐 |
| Stack                            | Vector를 상속받아 구현                                       |
| Queue                            | LinkedList가 Queue인터페이스 구현                            |
| Properties                       | Hashtable을 상속받아 구현                                    |
| HashSet                          | HashMap을 이용해서 구현                                      |
| TreeSet                          | TreeMap을 이용해서 구현                                      |
| LinkedHashMap<br />LinkedHashSet | HashMap과 HashSet에 저장순서 유지기능 추가                   |

