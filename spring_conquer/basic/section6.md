## 컴포넌트 스캔

- **컴포넌트 스캔과 의존관계 자동 주입 시작하기**

  - 설정 정보 없어도 자동으로 스프링 빈을 등록하는 컴포넌트 스캔

  ```java
  @Configuration
  @ComponentScan(
  	excludeFilters = @Filter(type = FilterType.ANNOTATION, classes = Configuration.class))
  public class AutoAppConfig {
      
  }
  ```

  - 컴포넌트 스캔을 사용하려면 `@ComponentScan`을 설정 정보에 붙여주면 됨
  - 기존의 `AppConfig`와 달리 `@Bean`으로 등록한 클래스가 없음
  - 참고: 섹션4에서 수동으로 만든 설정정보 제외를 위해 `excludeFilters`옵션 사용
  - `@Configuration`안에도 `@Component`가 붙어있음
  - 컴포넌스 스캔의 대상이 되는 클래스에 `@Component`를 붙여줌
  - 생성자에 `@Autowired`를 통해 자동으로 의존관계를 주입 해준다.
  - `@ComponentScan`
    - `@Component`가 붙은 모든 클래스를 스프링 빈으로 등록
    - 빈 이름 기본 전략: `MemberServiceImpl 클래스` -> `memberServiceImpl`
    - 빈 이름 직접 지정: `@Component("memberService2")`
  - `@Autowired`
    - 스프링 컨테이너가 자동으로 해당 스프링 빈을 찾아서 주입
    - 기본 조회 전략: 타입이 같은 빈을 찾아서 주입
      - `getBean(MemberRepository.class)` 와 동일하다고 보면 됨
    - 생성자에 파라미터가 많아도 다 찾아서 자동 주입

- **탐색 위치와 기본 스캔 대상**

- **필터**

- **중복 등록과 충돌**

