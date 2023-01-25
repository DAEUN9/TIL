## 의존관계 자동 주입

- **다양한 의존관계 주입 방법**

  - 생성자 주입

    - 생성자 호출시점에 딱 1번만 호출되는 것이 보장
    - **불변, 필수** 의존관계에 주로 사용
    - 생성자가 1개 있으면 `@Autowired` 생략 가능

  - 수정자 주입(setter 주입)

    - 생성자 호출 이후 호출됨
    - **선택, 변경** 가능성이 있을때 사용

    ```java
    @Autowired
    public void setMemberRepository(MemberRepository memberRepository) {
    	this.memberRepository = memberRepository;
    }
    
    // set~ , get~ : 자바빈 프로퍼티 규약
    ```

  - 필드 주입

    - 필드에 `@Autowired`를 달아줌

    - 스프링 컨테이너가 관리하는 인스턴스만 가져올 수 있음

    - 단점

      - 테스트하기 힘들다

      - `DI` 컨테이너 없으면 아무것도 못함

    - 사용하지 말자, 사용해도 되는 곳은

      - 실재 코드와 관계 없는 테스트 코드
        - `@SpringBootTest`처럼 스프링 컨테이너를 테스트에 통합한 경우만 가능
      - `@Configuration`

  - 일반 메서드 주입

    - 일반 메서드를 통해서 주입을 받을 수 있음
    - 특징
      - 한번에 여러 필드를 주입 받을 수 있음
      - 잘 안씀
    - 의존관계 자동 주입은 스프링 컨테이너가 관리하는 스프링 빈이어야 동작

    

- **옵션 처리**

  - `@Autowired`만 사용하면 기본적으로 `required`가 `true`
    - 자동 주입 대상이 없으면 오류 발생
  - 자동 주입 대상을 옵션으로 처리하는 방법
    - `@Autowired(required=false)` : 자동 주입할 대상이 없으면 수정자 메서드 자체가 호출 안됨
    - `org.springframework.lang.@Nullable` : 자동 주입할 대상이 없으면 `null`이 입력된다.
    - `Optional<>` : 자동 주입할 대상이 없으면 `Optional.empty`가 입력된다.

  ```java
  // 호출 안됨
  @Autowired(required = false)
  public void setNoBean1(Member member) {
      System.out.println(member);
  }
  
  // null 호출
  @Autowired
  public void setNobean(@Nullable Member member) {
      System.out.println(member);
  }
  
  // Optional.empty 호출
  @Autowired(required = false)
  public void setNoBean3(Optional<Member> member) {
      System.out.println(member);
  }
  ```

  

- **생성자 주입을 선택해라!**

  - 스프링을 포함한 `DI` 프레임워크 대부분이 생성자 주입 권장

  - **불변**

    - 대부분의 의존관계 주입은 한번 일어나면 애플리케이션 종료 전까지 불변해야 한다,
    - 수정자 주입을 사용하면, setXxx 메서드를 public으로 열어두어야 함
    - 누군가 실수로 변결하 수도 있고, 변경하면 안되는 메서드를 열어두는 것은 좋은 설계 방법이 아님
    - 생성자 주입은 객체를 생성할 때 딱 1번만 호출되므로 이후에 호출되는 일이 없다 -> 불변하게 설계 가능

  - **누락**

    - 생성자 주입을 사용하면 주입 데이터를 누락 했을 때 컴파일 오류 발생
      - IDE에서 바로 어떤 값을 필수로 주입해야 하는지 알 수 있음

  - **final**

    - 생성자 주입을 사용하면 필드에 `final` 사용 가능

    - 생성자에서 혹시라도 값이 설정되지 않는 오류를 컴파일 시점에서 막아줌

    - 나머지 주입 방식은 `final` 사용 불가

      - 모두 생성자 이후에 호출되므로

      

- **롬복과 최신 트랜드**

  - `@RequiredArgsConstructor` : `final`이 붙은 필드를 모아서 생성자를 자동으로 만들어 줌

  

- **조회 빈이 2개 이상 - 문제**

  - `@Autowired`는 타입으로 조회

    - 같은 타입 빈이 여러 개 발견되면 오류 발생

    

- **@Autowired 필드 명, @Qualifier, @Primary**

  - 조회 대상 빈이 2개 이상일 때 해결방법

    - `@Autowired` 필드 명 매칭

      - 타입 매칭 시도 후 여러 빈이 있으면 필드 이름, 파라미트 이름으로 빈 이름을 추가 매칭

    - `@Qualifier` -> `@Qualifier`끼리 매칭 -> 빈 이름으로 매칭

      - 주입시 추가적인 방법을 제공하는 것이지 빈 이름을 변경하는 것은 아님
      - 클래스, 생성자, 수정자에도 사용 가능
      - `@Qualifier`는 `@Qualifier`를 찾는 용도로만 명확하게 사용하자

      ```java
      @Component
      @Qualifier("mainDiscountPolicy")
      public class RateDiscountPolicy implements DiscountPolicy {}
      ```

    - `@Primary` : 우선순위를 정하는 방법

    - `@Primary` vs `@Qualifier`

      - `@Primary` : 자주 사용하는 메인 DB 커넥션을 획득하는 빈
        - 기본값처럼 동작
      - `@Qualifier` : 특별한 기능에서 가끔 사용하는 서브 DB 커넥션을 획득하는 빈
        - 매우 상세하게 동작

    - 우선순위

      - `@Qualifier` > `@Primary`
      - 스프링은 자동보다는 수동이, 넓은 범위 보다는 좁은 범위의 선택권이 우선

      

- **애노테이션 직접 만들기**

  - 문자열로 이름을 지정하는 것보다 에러 잡기 쉬움
    - 오타시 애노테이션은 컴파일 에러가 남
  - 애노테이션은 상속이라는 개념이 없음

  

- **조회한 빈이 모두 필요할 때, List, Map**

  ```java
  static class DiscountService {
      private final Map<String, DiscountPolicy> policyMap;
      private final List<DiscountPolicy> policies;
      
      public DiscountService(Map<String, DiscountPolicy> policyMap, List<DiscountPolicy> policies) {
          this.policyMap = policyMap;
          this.policies = policies;
      }
      
      public int discount(Member member, int price, String discountCode) {
          
          Discount discountPolicy = policyMap.get(discountCode);
          
          return discountPolicy.discount(member, price);
      }
  }
  ```

  - 로직 분석

    - `DiscountService`는 Map으로 모든 `DiscountPolicy`를 주입 받음
    - `discount()`는 `discountCode`에 "fixDiscountPolicy"나 "rateDiscountPolicy"를 넘겨줌

  - 주입 분석

    - `Map<String, DiscountPolicy>` : map의 키에 스프링 빈의 이름을 넣어주고, 그 값으로 `DiscountPolicy` 타입으로 조회한 모든 스프링 빈을 담아줌
    - `List<DiscountPolicy>` : `DiscountPolicy` 타입으로 조회한 모든 스프링 빈을 담아줌
    - 해당하는 타입의 스프링 빈이 없으면, 빈 컬렉션이나 Map을 주입

    

- **자동, 수동의 올바른 실무 운영 기준**

  - 편리한 자동 기능을 기본으로 사용하자

    - 자동 빈 등록을 사용해도 `OCP`, `DIP`를 지킬 수 있다.

  - 업무 로직 빈 : 비즈니스 요구사항을 개발할 때 추가되거나 변경되는 빈

    - 자동 기능 적극 사용

  - 기술 지원 빈 : 기술적인 문제나 `AOP`를 처리할 때 주로 사용

    - 수동 빈 등록으로 명확하게 드러냄

  - 애플리케이션에 광범위하게 영향을 미치는 기술 지원 객체는 수동 빈으로 등록해서 설정 정보에 바로 나타나게 하는 것이 좋음

  - 비즈니스 로직 중 다형성을 적극 활용할 때

    - 기술 지원 빈은 수동 빈이나, 자동 빈 등록 후 특정 패키지에 묶어두기
    - 한눈에 빈 이름과 어떤 빈들이 주입될지 파악

    ```java
    // 수동등록
    
    @Configuration
    public class DiscountPolicyConfig {
        
        @Bean
        public DiscountPolicy rateDiscountPolicy() {
            return new RateDiscountPolicy();
        }
        
        @Bean
        public DiscountPolicy fixDiscountPolicy() {
            return new FixDiscountPolicy();
        }
    }
    ```

  - 스프링과 스프링 부트가 자동으로 등록하는 빈들은 예외