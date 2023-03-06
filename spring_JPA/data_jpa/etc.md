## 나머지 기능들

> 실무에서는 잘 사용하지 않음

- Specifications(명세)

  - 스프링 데이터 JPA는 JPA Criteria를 활용해서 이 개념을 사용할 수 있도록 지원

  - 술어(predicate)

    - 참 또는 거짓으로 평가
    - AND OR 같은 연산자로 조합해서 다양한 검색조건을 쉽게 생성(컴포지트 패턴)
    - 스프링 데이터 JPA는 `org.springframework.data.jpa.domain.Specification` 클래스로 정의

  - 명세 기능 사용 방법

    - `JpaSpecificationExecutor` 인터페이스 상속

      ```java
      public interface MemberRepository extends JpaRepository<Member, Long>,
       
      JpaSpecificationExecutor<Member> {
       
      }
      ```

    - ` JpaSpecificationExecutor 인터페이스`

      ```java
      public interface JpaSpecificationExecutor<T> {
          Optional<T> findOne(@Nullable Specification<T> spec);
          List<T> findAll(Specification<T> spec);
          Page<T> findAll(Specification<T> spec, Pageable pageable);
          List<T> findAll(Specification<T> spec, Sort sort);
          long count(Specification<T> spec);
      }
      ```

      - `Specification` 을 파라미터로 받아서 검색 조건으로 사용
      - `Specification` 을 구현하면 명세들을 조립할 수 있음. `where()` , `and()` , `or()` , `not()` 제공

    - 사용 예제 일부

      ```java
      Specification<Member> spec =
          MemberSpec.username("m1").and(MemberSpec.teamName("teamA"));
      List<Member> result = memberRepository.findAll(spec);
      ```

    - `MemberSpec` 명세 정의 코드

      ```java
      public class MemberSpec {
          public static Specification<Member> teamName(final String teamName) {
              return (Specification<Member>) (root, query, builder) -> {
                  if (StringUtils.isEmpty(teamName)) {
                      return null;
                  }
                  Join<Member, Team> t = root.join("team", JoinType.INNER); //회원과 조인
                      return builder.equal(t.get("name"), teamName);
              };
          }
          public static Specification<Member> username(final String username) {
              return (Specification<Member>) (root, query, builder) ->
                  builder.equal(root.get("username"), username);
          }
      }
      ```

      - 명세를 정의하려면 `Specification` 인터페이스를 구현
      - 명세를 정의할 때는 `toPredicate(...)` 메서드만 구현하면 됨
        - JPA Criteria의 `Root`, `CriteriaQuery`, `CriteriaBuilder` 클래스 파라미터 제공
      - 예제에서는 편의상 람다 사용

  - 참고

    - 실무에서는 대신 **QueryDSL**을 사용하자



- Query By Example

  > 사용자가 원하는 데이터를 예시로 제공하여 데이터베이스가 이를 기반으로 적합한 결과를 반환

  - 테스트

    ```java
    @SpringBootTest
    @Transactional
    public class QueryByExampleTest {
        
        @Autowired MemberRepository memberRepository;
        @Autowired EntityManager em;
        @Test
        
        public void basic() throws Exception {
            
            //given
            Team teamA = new Team("teamA");
            em.persist(teamA);
            em.persist(new Member("m1", 0, teamA));
            em.persist(new Member("m2", 0, teamA));
            em.flush();
            
            //when
            //Probe 생성
            Member member = new Member("m1");
            Team team = new Team("teamA"); //내부조인으로 teamA 가능
            member.setTeam(team);
            
            //ExampleMatcher 생성, age 프로퍼티는 무시
            ExampleMatcher matcher = ExampleMatcher.matching()
                .withIgnorePaths("age");
            Example<Member> example = Example.of(member, matcher);
            List<Member> result = memberRepository.findAll(example);
            
            //then
            assertThat(result.size()).isEqualTo(1);
        }
    }
    ```

    - `Probe` : 필드에 데이터가 있는 실제 도메인 객체
    - `ExcampleMatcher` : 특정 필드를 일치시키는 상세한 정보 제공, 재사용 가능
    - `Example` : `Probe`와 `ExampleMatcher`로 구성, 쿼리를 생성

  - 장점

    - 동적 쿼리를 편리하게 처리
    - 도메인 객체를 그대로 사용
    - 데이터 저장소를 RDB에서 NOSQL로 변경해도 코드 변경이 없게 추상화 되어 있음 
    - 프링 데이터 JPA `JpaRepository` 인터페이스에 이미 포함

  - 단점

    - 조인은 가능하지만 내부 조인(INNER JOIN)만 가능함 외부 조인(LEFT JOIN) 안됨
    - 다음과 같은 중첩 제약조건 안됨
      - `firstname = ?0 or (firstname = ?1 and lastname = ?2)`
    - 매칭 조건이 매우 단순함
      - 문자는 `starts/contains/ends/regex`
      - 다른 속성은 정확한 매칭( `=` )만 지원

  - 실무에서는 QueryDSL을 사용하자



- Projections

  > 엔티티 대신에 DTO를 편리하게 조회

  - 전체 엔티티가 아니라 회원 이름만 조회하고 싶으면?

    ```java
    public interface UsernameOnly {
        String getUsername();
    }
    ```

    - 조회할 엔티티 필드를 getter형식으로 지정하면 해당 필드만 선택해서 조회
      - Proejction

    ```java
    public interface MemberRepository ... {
        List<UsernameOnly> findProjectionsByUsername(String username);
    }
    ```

    - 메서드 이름은 자유, 반환 타입으로 인지

    ```java
    @Test
    public void projections() throws Exception {
        
        //given
        Team teamA = new Team("teamA");
        em.persist(teamA);
        Member m1 = new Member("m1", 0, teamA);
        Member m2 = new Member("m2", 0, teamA);
        em.persist(m1);
        em.persist(m2);
        em.flush();
        em.clear();
        
        //when
        List<UsernameOnly> result =
            memberRepository.findProjectionsByUsername("m1");
        
        //then
        Assertions.assertThat(result.size()).isEqualTo(1);
    }
    ```

    - username만 조회됨