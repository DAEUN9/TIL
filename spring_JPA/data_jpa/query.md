## 쿼리 메소드 기능

- 메소드 이름으로 쿼리 생성

  - 순수 JPA 레포지토리

    ```java
    public List<Member> findByUsernameAndAgeGreaterThan(String username, int age) {
     return em.createQuery("select m from Member m where m.username = :username and m.age > :age")
     .setParameter("username", username)
     .setParameter("age", age)
     .getResultList();
    }
    ```

  - 스프링 데이터 JPA

    ```java
    public interface MemberRepository extends JpaRepository<Member, Long> {
        List<Member> findByUsernameAndAgeGreaterThan(String username, int age);
    }
    ```

    - 스프링 데이터 JPA는 메소드 이름을 분석해서 JPQL을 생성하고 실행

  - 스프링 데이터 JPA가 제공하는 쿼리 메소드 기능

    - 조회: find…By ,read…By ,query…By get…By
    - COUNT: count…By 반환타입 `long`
    - EXISTS: exists…By 반환타입 `boolean`
    - 삭제: delete…By, remove…By 반환타입 `long`
    - DISTINCT: findDistinct, findMemberDistinctBy
    - LIMIT: findFirst3, findFirst, findTop, findTop3

  - 참고

    - 엔티티의 필드명이 변경되면 인터페이스에 정의한 메서드 이름도 꼭 함께 변경해야 한다
    - 이렇게 애플리케이션 로딩 시점에 오류를 인지할 수 있는 것이 스프링 데이터 JPA의 매우 큰 장점



- JPA NamedQuery

  - 실무에서 쓸 일은 별로 없음

  - 애플리케이션 실행 시점에 쿼리 파싱(정적쿼리)을 하기 때문에 오타 오류를 잡을 수 있음

    ```java
    @Entity
    @NamedQuery(
        name="Member.findByUsername",
        query="select m from Member m where m.username = :username")
    public class Member {
        ...
    }
    ```

  - 스프링 데이터 JPA로 NamedQuery 사용

    ```java
    @Query(name = "Member.findByUsername")
    List<Member> findByUsername(@Param("username") String username);
    ```

    - `@Query` 를 생략하고 메서드 이름만으로 Named 쿼리를 호출할 수 있다.
    - 스프링 데이터 JPA는 선언한 "도메인 클래스 + `.`(점) + 메서드 이름"으로 Named 쿼리를 찾아서 실행
    - 만약 실행할 Named 쿼리가 없으면 메서드 이름으로 쿼리 생성 전략을 사용
    - 필요하면 전략을 변경할 수 있지만 권장하지 않는다.
    - 실무에서는 `@Query` 를 사용해서 리파지토리 메소드에 쿼리를 직접 정의



- `@Query`, 리포지토리 메소드에 쿼리 정의하기

  ```java
  public interface MemberRepository extends JpaRepository<Member, Long> {
      @Query("select m from Member m where m.username= :username and m.age = :age")
      List<Member> findUser(@Param("username") String username, @Param("age") int age);
  }
  ```

  - 실행할 메서드에 정적 쿼리를 직접 작성하므로 이름 없는 Named 쿼리라 할 수 있음
  - JPA Named 쿼리처럼 애플리케이션 실행 시점에 문법 오류를 발견할 수 있음(매우 큰 장점!)
  - 실무에서는 파라미터가 증가하면서 메서드 이름이 지저분 해짐
    - `@Query` 기능을 자주 사용하게 된다



- `@Query` 값, DTO 조회하기

  - 단순히 값 하나 조회

    ```java
    @Query("select m.username from Member m")
    List<String> findUsernameList();
    ```

    - JPA 값 타입( `@Embedded` )도 이 방식으로 조회할 수 있다

  - DTO로 직접 조회

    ```java
    @Query("select new study.datajpa.dto.MemberDto(m.id, m.username, t.name) " +
           "from Member m join m.team t")
    List<MemberDto> findMemberDto();
    ```

    - DTO로 직접 조회 하려면 JPA의 `new `명령어를 사용해야 한다
    - 생성자가 맞는 DTO 필요



- 파라미터 바인딩

  ```java
  select m from Member m where m.username = ?0 //위치 기반
  select m from Member m where m.username = :name //이름 기반
  ```

  - 코드 가독성과 유지보수를 위해 이름 기반 파라미터 바인딩을 사용하자

  - 컬렉션 파라미터 바인딩

    - `Collection` 타입으로 in 절 지원

    ```java
    @Query("select m from Member m where m.username in :names")
    List<Member> findByNames(@Param("names") List<String> names);
    ```

  - 조회 결과가 많거나 없으면?
    - 컬렉션
      - 결과 없음 : 빈 컬렉션 반환
    - 단건 조회
      - 결과 없음 : `null` 반환
      - 결과가 2건 이상 : `: javax.persistence.NonUniqueResultException` 예외 발생



- 순수 JPA 페이징과 정렬

  ```java
  public List<Member> findByPage(int age, int offset, int limit) {
      return em.createQuery("select m from Member m where m.age = :age order by m.username desc")
                            .setParameter("age", age)
                            .setFirstResult(offset)
                            .setMaxResults(limit)
                            .getResultList();
                            }
                            public long totalCount(int age) {
                                return em.createQuery("select count(m) from Member m where m.age = :age",
                                                      Long.class)
                                    .setParameter("age", age)
                                    .getSingleResult();
                            }
  ```

- 스프링 데이터 JPA 페이징과 정렬

  - 페이징과 정렬 파라미터

    - `org.springframework.data.domain.Sort` : 정렬 기능 
    - `org.springframework.data.domain.Pageable` : 페이징 기능 (내부에 `Sort` 포함)

  - 특별한 반환 타입

    - `org.springframework.data.domain.Page` : 추가 count 쿼리 결과를 포함하는 페이징 
    - `org.springframework.data.domain.Slice` : 추가 count 쿼리 없이 다음 페이지만 확인 가능
      - (내부적으로 limit + 1조회)
    - `List` (자바 컬렉션): 추가 count 쿼리 없이 결과만 반환

  - 사용 예제

    ```java
    Page<Member> findByUsername(String name, Pageable pageable); //count 쿼리 사용
    Slice<Member> findByUsername(String name, Pageable pageable); //count 쿼리 사용 안함
    List<Member> findByUsername(String name, Pageable pageable); //count 쿼리 사용 안함
    List<Member> findByUsername(String name, Sort sort);
    Page<Member> findByAge(int age, Pageable pageable);
    ```

    ```java
    // 페이징 조건과 ㅏ정렬 조건 설정
    @Test
    public void page() throws Exception {
        
        //given
        memberRepository.save(new Member("member1", 10));
        memberRepository.save(new Member("member2", 10));
        memberRepository.save(new Member("member3", 10));
        memberRepository.save(new Member("member4", 10));
        memberRepository.save(new Member("member5", 10));
        
        //when
        PageRequest pageRequest = PageRequest.of(0, 3, Sort.by(Sort.Direction.DESC,
                                                               "username")); // page, size ...
        Page<Member> page = memberRepository.findByAge(10, pageRequest); // 
        
        //then
        List<Member> content = page.getContent(); //조회된 데이터
        assertThat(content.size()).isEqualTo(3); //조회된 데이터 수
        assertThat(page.getTotalElements()).isEqualTo(5); //전체 데이터 수
        assertThat(page.getNumber()).isEqualTo(0); //페이지 번호
        assertThat(page.getTotalPages()).isEqualTo(2); //전체 페이지 번호
        assertThat(page.isFirst()).isTrue(); //첫번째 항목인가?
        assertThat(page.hasNext()).isTrue(); //다음 페이지가 있는가?
    }
    ```

    - 두 번째 파라미터로 받은 `Pageable` 은 인터페이스다
      - 따라서 실제 사용할 때는 해당 인터페이스를 구현한 `org.springframework.data.domain.PageRequest` 객체를 사용한다
    - `PageRequest` 생성자의 첫 번째 파라미터에는 현재 페이지를, 두 번째 파라미터에는 조회할 데이터 수
      - 여기에 추가로 정렬 정보도 파라미터로 사용할 수 있다. 참고로 페이지는 0부터 시작
    - `Slice`는 limit +1 값을 조회

  - Page 인터페이스

    ```java
    public interface Page<T> extends Slice<T> {
        int getTotalPages(); //전체 페이지 수
        long getTotalElements(); //전체 데이터 수
        <U> Page<U> map(Function<? super T, ? extends U> converter); //변환기
    }
    ```

  - Slice 인터페이스

    ```java
    public interface Slice<T> extends Streamable<T> {
        int getNumber(); //현재 페이지
        int getSize(); //페이지 크기
        int getNumberOfElements(); //현재 페이지에 나올 데이터 수
        List<T> getContent(); //조회된 데이터
        boolean hasContent(); //조회된 데이터 존재 여부
        Sort getSort(); //정렬 정보
        boolean isFirst(); //현재 페이지가 첫 페이지 인지 여부
        boolean isLast(); //현재 페이지가 마지막 페이지 인지 여부
        boolean hasNext(); //다음 페이지 여부
        boolean hasPrevious(); //이전 페이지 여부
        Pageable getPageable(); //페이지 요청 정보
        Pageable nextPageable(); //다음 페이지 객체
        Pageable previousPageable();//이전 페이지 객체
        <U> Slice<U> map(Function<? super T, ? extends U> converter); //변환기
    }
    ```

  - count 쿼리를 분리할 수 있음

    ```java
    @Query(value = “select m from Member m”,
           countQuery = “select count(m.username) from Member m”)
    Page<Member> findMemberAllCountBy(Pageable pageable);
    ```

    - 복잡한 sql에 사용
    - 데이터는 left join 하고, 카운트는 left join 안해도 됨

  - 페이지를 유지하면서 엔티티를 DTO로 변환하기

    ```java
    Page<Member> page = memberRepository.findByAge(10, pageRequest);
    Page<MemberDto> dtoPage = page.map(m -> new MemberDto());
    ```



- 벌크성 수정 쿼리

  ```java
  // JPA 사용
  public int bulkAgePlus(int age) {
      int resultCount = em.createQuery(
          "update Member m set m.age = m.age + 1" +
          "where m.age >= :age")
          .setParameter("age", age)
          .executeUpdate();
      return resultCount;
  }
  ```

  ```java
  // 스프링 데이터 JPA 사용
  @Modifying
  @Query("update Member m set m.age = m.age + 1 where m.age >= :age")
  int bulkAgePlus(@Param("age") int age);
  ```

  - 한번에 몽땅 수정 -> DB에 날리기

  - `executeUpdate()` 와 `@Modifying`이 비슷한 기능

  - 벌크성 수정, 삭제 쿼리는 `@Modifying` 어노테이션을 사용

    - 사용하지 않으면 예외 발생

  - 벌크성 쿼리를 실행하고 나서 영속성 컨텍스트 초기화: `@Modifying(clearAutomatically = true)`

    - 기본값은 `false`

  - 벌크성 쿼리를 실행하고 다시 조회해야 한다면 꼭 영속성 컨텍스트를 초기화 하자

    - 벌크 연산은 영속성 컨텍스트 상관없이 벌크 연산을 DB로 날림

    - 영속성 컨텍스트에 과거 값이 남아서 문제가 생길 수 있음

      - 엔티티의 상태와 DB에 엔티티 상태가 달라질 수 있음

    - 방안

      1. 영속성 컨텍스트에 엔티티가 없는 상태에서 벌크 연산을 먼저 실행한다. 
      2. 부득이하게 영속성 컨텍스트에 엔티티가 있으면 벌크 연산 직후 영속성 컨텍스트를 초기화 한다.

      - 쿼리 날리기 전에 flush나 clear하기



- `@EntityGraph`

  - 연관된 엔티티들을 SQL 한번에 조회하는 방법

  - 참고

    - 다음과 같이 지연 로딩 여부를 확인할 수 있음

    ```java
    //Hibernate 기능으로 확인
    Hibernate.isInitialized(member.getTeam());
    
    //JPA 표준 방법으로 확인
    PersistenceUnitUtil util =
        em.getEntityManagerFactory().getPersistenceUnitUtil();
    util.isLoaded(member.getTeam());
    ```

  - `EntityGraph`

    ```java
    //공통 메서드 오버라이드
    @Override
    @EntityGraph(attributePaths = {"team"})
    List<Member> findAll();
    
    //JPQL + 엔티티 그래프
    @EntityGraph(attributePaths = {"team"})
    @Query("select m from Member m")
    List<Member> findMemberEntityGraph();
    
    //메서드 이름으로 쿼리에서 특히 편리하다.
    @EntityGraph(attributePaths = {"team"})
    List<Member> findByUsername(String username)
    ```

    - 사실상 페치 조인(FETCH JOIN)의 간편 버전
    - LEFT OUTER JOIN 사용

  - `NamedEntityGraph` 사용 방법

    ```java
    @NamedEntityGraph(name = "Member.all", attributeNodes =
                      @NamedAttributeNode("team"))
    @Entity
    public class Member {}
    ```

    ```java
    @EntityGraph("Member.all")
    @Query("select m from Member m")
    List<Member> findMemberEntityGraph();
    ```



- JPA Hint & Lock

  - JPA Hint

    - JPA 쿼리 힌트(SQL 힌트가 아니라 JPA 구현체에게 제공하는 힌트)

  - 쿼리 힌트 사용

    ```java
    @QueryHints(value = @QueryHint(name = "org.hibernate.readOnly",
                                   value = "true"))
    Member findReadOnlyByUsername(String username);
    ```

    ```java
    @Test
    public void queryHint() throws Exception {
        //given
        memberRepository.save(new Member("member1", 10));
        em.flush();
        em.clear();
        
        //when
        Member member = memberRepository.findReadOnlyByUsername("member1");
        member.setUsername("member2");
        
        em.flush(); //Update Query 실행X
    }
    ```

  - 쿼리 힌트 Page 추가 예제

    ```java
    @QueryHints(value = { @QueryHint(name = "org.hibernate.readOnly",
                                     value = "true")},
                forCounting = true)
    Page<Member> findByUsername(String name, Pageable pageable);
    ```

    - `forCounting` : 반환 타입으로 Page 인터페이스를 적용하면 추가로 호출하는 count  쿼리도 쿼리 힌트 적용(기본값 true )

    - 스냅샷을 만들지 않고 변경감지 체크 안함
      - 내부적으로 읽기에 최적화

  - 성능테스트를 해보고 적용할지 결정하자

    - 만약 캐시가 부족하면 실제로는 redis를 앞에 깔든가 해야함

- Lock

  ```java
  @Lock(LockModeType.PESSIMISTIC_WRITE)
  List<Member> findByUsername(String name);
  ```

  - 실시간 서비스에서는 Lock을 걸지 말자
    - 낙관적 락을 걸거나 다른 방법 사용

