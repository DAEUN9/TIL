## 확장 기능

- 사용자 정의 리포지토리 구현

  - 다양한 이유로 인터페이스의 메서드를 직접 구현하고 싶다면?

    - JPA 직접 사용( EntityManager )
    - 스프링 JDBC Template 사용
    - MyBatis 사용
    - 데이터베이스 커넥션 직접 사용 등등...
    - Querydsl 사용

  - 사용자 정의 인터페이스

    ```java
    public interface MemberRepositoryCustom {
        List<Member> findMemberCustom();
    }
    
    ```

  - 사용자 정의 인터페이스 구현 클래스

    ```java
    @RequiredArgsConstructor
    public class MemberRepositoryImpl implements MemberRepositoryCustom {
        
        private final EntityManager em;
        
        @Override
        public List<Member> findMemberCustom() {
            return em.createQuery("select m from Member m")
                .getResultList();
        }
    }
    ```

  - 사용자 정의 인터페이스 상속

    ```java
    public interface MemberRepository
        extends JpaRepository<Member, Long>, MemberRepositoryCustom {
    }
    ```

    - 인터페이스들을 상속

  - 사용자 정의 메서드 호출 코드

    ```java
    List<Member> result = memberRepository.findMemberCustom();
    ```

  - 사용자 정의 구현 클래스

    - 규칙 : 리포지토리 인터페이스 이름 + `Impl`

    - 스프링 데이터 JPA가 인식해서 스프링 빈으로 등록

    - 다른 이름으로 변경하고 싶으면?

      - xml 설정

        ```xml
        <repositories base-package="study.datajpa.repository"
         repository-impl-postfix="Impl" />
        ```

        - 웬만하면 바꾸지 말고 관례를 따르자

      - JavaConfig 설정

        ```java
        @EnableJpaRepositories(basePackages = "study.datajpa.repository",
                               repositoryImplementationPostfix = "Impl")
        ```

  - 참고
    - 실무에서는 `QueryDSL`이나 `SpringJdbcTemplate`을 함께 사용할 때 사용자 정의 리포지토리 자주 사용
    - 항상 필요한 것은 아님
      - 복잡해서 분리가 필요할 때 사용



- 최신 사용자 정의 리포지토리 구현 방식

  - 스프링 데이터 2.x 부터는 사용자 정의 인터페이스 명 + `Impl` 방식도 지원

  - 예제의 `MemberRepositoryImpl` 대신에 `MemberRepositoryCustomImpl` 같이 구현해도 된다

    ```java
    @RequiredArgsConstructor
    public class MemberRepositoryCustomImpl implements MemberRepositoryCustom {
        
        private final EntityManager em;
        
        @Override
        public List<Member> findMemberCustom() {
            return em.createQuery("select m from Member m")
                .getResultList();
        }
    }
    
    ```

    - 기존 방식보다 직관적
    - 여러 인터페이스를 분리해서 구현하는 것도 가능하기 때문에 이 방식 권장



- Auditing

  - 엔티티를 생성, 변경할 때 변경한 사람과 시간을 추적하고 싶으면?

  - 이벤트 리스너는 엔티티가 변경될 때 이벤트를 수신하고, 이벤트 핸들러를 호출하여 엔티티의 상태를 변경

    - 등록일
    - 수정일
    - 등록자
    - 수정자

  - 순수 JPA 사용

    - 등록일 ,수정일

    ```java
    package study.datajpa.entity;
    
    @MappedSuperclass
    @Getter
    public class JpaBaseEntity {
        
        @Column(updatable = false)
        private LocalDateTime createdDate;
        private LocalDateTime updatedDate;
        
        @PrePersist
        public void prePersist() {
            LocalDateTime now = LocalDateTime.now();
            createdDate = now;
            updatedDate = now;
        }
        
        @PreUpdate
        public void preUpdate() {
            updatedDate = LocalDateTime.now();
        }
    }
    
    ```

    ```java
    public class Member extends JpaBaseEntity {}
    ```

    - `@MappedSuperclass`
      - 속성만 상속 받아서 사용하고 싶을 때
      - 엔티티가 아님, 테이블과 매핑도 안됨
      - 직접 생성해서 사용할 일이 없으므로 추상 클래스로 만드는 것을 권장

  - JPA 주요 이벤트 어노테이션

    - `@PrePersist`
      - 엔티티가 영구 저장되기 전에 호출
    - `@PostPersist`
      - 엔티티가 영구 저장된 후에 호출
    - `@PreUpdate`
      - 엔티티가 업데이트되기 전에 호출
    - `@PostUpdate`
      - 엔티티가 업데이트된 후에 호출



- Auditing 스프링 데이터 JPA 사용

  - 설정

  - `@EnableJpaAuditing`

    - 스프링 부트 설정 클래스에 적용해야함 

  - `@EntityListeners(AuditingEntityListener.class)`

    - 엔티티에 적용

  - 사용 어노테이션

    - `@CreatedDate`
      - 엔티티가 생성된 시간을 기록
    - `@LastModifiedDate`
      - 엔티티가 마지막으로 수정된 시간을 기록
    - `@CreatedBy`
      - 엔티티를 생성한 사용자를 기록
    - `@LastModifiedBy`
      - 엔티티를 마지막으로 수정한 사용자를 기록

  - 등록일, 수정일

    ```java
    package study.datajpa.entity;
    
    @EntityListeners(AuditingEntityListener.class)
    @MappedSuperclass
    @Getter
    public class BaseEntity {
        
        @CreatedDate
        @Column(updatable = false)
        private LocalDateTime createdDate;
        
        @LastModifiedDate
        private LocalDateTime lastModifiedDate;
    }
    ```

  - 등록자, 수정자

    ```java
    package jpabook.jpashop.domain;
    
    @EntityListeners(AuditingEntityListener.class)
    @MappedSuperclass
    public class BaseEntity {
        
        @CreatedDate
        @Column(updatable = false)
        private LocalDateTime createdDate;
        
        @LastModifiedDate
        private LocalDateTime lastModifiedDate;
        
        @CreatedBy
        @Column(updatable = false)
        private String createdBy;
        
        @LastModifiedBy
        private String lastModifiedBy;
    }
    ```

  - 등록자, 수정자를 처리해주는 `AuditorAware` 스프링 빈 등록

    ```java
    @Bean
    public AuditorAware<String> auditorProvider() {
        return () -> Optional.of(UUID.randomUUID().toString());
    }
    ```

    - 실무에서는 세션 정보나, 스프링 시큐리티 로그인 정보에서 ID를 받음

  - 실무에서 등록시간, 수정시간은 거의 필수지만, 등록자 수정자는 없을 수도 있음

    - Base 타입 분리

    ```java
    public class BaseTimeEntity {
        @CreatedDate
        @Column(updatable = false)
        private LocalDateTime createdDate;
        @LastModifiedDate
        private LocalDateTime lastModifiedDate;
    }
    
    public class BaseEntity extends BaseTimeEntity {
        @CreatedBy
        @Column(updatable = false)
        private String createdBy;
        @LastModifiedBy
        private String lastModifiedBy;
    }
    ```

    - 저장시점에 등록일, 등록자는 물론이고, 수정일, 수정자도 같은 데이터가 저장
    - 변경 컬럼만 확인해도 마지막에 업데이트한 유저를 확인 할 수 있으므로 유지보수 관점에서 편리

  - 전체 적용

    - `@EntityListeners(AuditingEntityListener.class)` 를 생략

    - 이벤트를 엔티티 전체에 적용하려면

    - `META-INF/orm.xml`

        ```java
        <?xml version=“1.0” encoding="UTF-8”?>
            <entity-mappings xmlns=“http://xmlns.jcp.org/xml/ns/persistence/orm”
        xmlns:xsi=“http://www.w3.org/2001/XMLSchema-instance”
        xsi:schemaLocation=“http://xmlns.jcp.org/xml/ns/persistence/orm http://xmlns.jcp.org/xml/ns/persistence/orm_2_2.xsd”
        version=“2.2">
            <persistence-unit-metadata>
            <persistence-unit-defaults>
            <entity-listeners>
            <entity-listener 
            class="org.springframework.data.jpa.domain.support.AuditingEntityListener”/>
                </entity-listeners>
                </persistence-unit-defaults>
                </persistence-unit-metadata>
        
                </entity-mappings>
        
        ```

      



- web 확장 - 도메인 클래스 컨버터

  > HTTP 파라미터로 넘어온 엔티티의 아이디로 엔티티 객체를 찾아서 바인딩

  ```java
  @RestController
  @RequiredArgsConstructor
  public class MemberController {
      private final MemberRepository memberRepository;
      @GetMapping("/members/{id}")
      public String findMember(@PathVariable("id") Member member) {
          return member.getUsername();
      }
  }
  
  ```

  - HTTP 요청은 회원 `id` 를 받지만 도메인 클래스 컨버터가 중간에 동작해서 회원 엔티티 객체를 반환
  - 도메인 클래스 컨버터도 리파지토리를 사용해서 엔티티를 찾음
  - 단순 조회용으로만 사용해야 함
    - 트랜잭션이 없는 범위에서 엔티티를 조회했으므로, 엔티티를 변경해도 DB에 반영X



- web 확장 - 페이징과 정렬

  ```java
  @GetMapping("/members")
  public Page<Member> list(Pageable pageable) {
      Page<Member> page = memberRepository.findAll(pageable);
      return page;
  }
  ```

  - 파라미터로 `Pageable` 을 받을 수 있다. 

  - `Pageable` 은 인터페이스, 실제는 `org.springframework.data.domain.PageRequest` 객체 생성

  - 요청 파라미터

    - 예) `/members?page=0&size=3&sort=id,desc&sort=username,desc`
    - `page`: 현재 페이지, 0부터 시작한다.
    - `size`: 한 페이지에 노출할 데이터 건수
    - `sort`: 정렬 조건을 정의한다.
      - 예) 정렬 속성,정렬 속성...(ASC | DESC)
      - 정렬 방향을 변경하고 싶으면 `sort` 파라미터 추가 ( `asc` 생략 가능)

  - 기본값

    - 글로벌 설정

      ```yaml
      spring.data.web.pageable.default-page-size=20 /# 기본 페이지 사이즈/
      spring.data.web.pageable.max-page-size=2000 /# 최대 페이지 사이즈/
      ```

    - 개별 설정

      ```java
      @RequestMapping(value = "/members_page", method = RequestMethod.GET)
      public String list(@PageableDefault(size = 12, sort = “username”,
                                          direction = Sort.Direction.DESC) Pageable pageable) {
          ...
      }
      ```

  - 접두사

    - 페이징 정보가 둘 이상이면 접두사로 구분

    - `@Qualifier` 에 접두사명 추가 `"{접두사명}_xxx`

    - 예제: `/members?member_page=0&order_page=1`

      ```java
      public String list(
          @Qualifier("member") Pageable memberPageable,
          @Qualifier("order") Pageable orderPageable, ...
      ```

  - Page 내용을 DTO로 변환하기

    - Page는 `map()` 지원

    - `Member DTO`

      ```java
      @Data
      public class MemberDto {
          private Long id;
          private String username;
          
          public MemberDto(Member m) {
              this.id = m.getId();
              this.username = m.getUsername();
          }
      }
      ```

    - `Page.map()` 사용

      ```java
      @GetMapping("/members")
      public Page<MemberDto> list(Pageable pageable) {
          Page<Member> page = memberRepository.findAll(pageable);
          Page<MemberDto> pageDto = page.map(MemberDto::new);
          return pageDto;
      }
      ```

    - 최적화

      ```java
      @GetMapping("/members")
      public Page<MemberDto> list(Pageable pageable) {
          return memberRepository.findAll(pageable).map(MemberDto::new);
      }
      ```

  - Page를 1부터 시작하기

    - 원래는 0부터 시작함

    1. Pageable, Page를 파리미터와 응답 값으로 사용히지 않고, 직접 클래스를 만들어서 처리

       - 직접 PageRequest(Pageable 구현체)를 생성해서 리포지토리에 넘긴다
       - Page 대신에 직접 만들어서 제공해야 한다

    2. `spring.data.web.pageable.one-indexed-parameters` 를 `true` 로 설정

       - web에서 `page` 파라미터를 `-1` 처리 할 뿐

       - 응답값인 `Page` 에 모두 0 페이지 인덱스를 사용하는 한계가 있다