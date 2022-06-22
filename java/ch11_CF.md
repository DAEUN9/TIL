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
- 