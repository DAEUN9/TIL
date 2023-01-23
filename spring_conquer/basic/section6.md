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

  - `@ComponentScan`의 `basePackages`를 통해 패키지 범위 설정 가능
    - 지정 안하면 현재 패키지부터 시작

  - `basePackageClass` : 지정한 클래스의 패키지를 탐색 시작 위로 지정

  - 권장하는 방법
    - 설정 정보 클래스 위치를 최상단에 두기
      - 하위는 모두 컴포넌트 스캔의 대상이 됨

    - `@SpringBootApplication`을 루트 패키지에 두는 것이 관례
      - 안에 `@ComponentScan`이 달려있음

  - 컴포넌트 스캔 기본 대상
    - `@Component`
    - `@Controller`
    - `@Service`
    - `@Repositorty`
      - DB에 접근하는 예외를 스프링 예외로 변환해줌

    - `@Configuration`

- **필터**

  - `includeFilter` : `ComponentScan` 대상 추가 지정

  - `excludeFilter` : 제외 대상 지정

- **중복 등록과 충돌**

  - 자동 빈 등록 vs 자동 빈 등록
    - 이름을 일부러 지정해주지 않으면 일어날 일 없음

  - 수동 빈 등록 vs 자동 빈 등록
    - 수동 등록 빈이 우선권을 가짐
    - 수동 빈이 자동 빈을 오버라이딩 해줌
    - 최근 스프링부트에서는 충돌이 나서 오류가 나도록 함


