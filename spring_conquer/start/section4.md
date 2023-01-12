## 스프링 빈과 의존관계

- 컴포넌트 스캔과 자동 의존관계 설정

  - `@Controller`, `@Service`, `@Repository`는 스프링이 뜰 때 컨테이너에 빈으로 자동 등록
  - 생성자에 `@Autowired`가 있으면 스프링컨테이너에 있는 것을 넣어줌
    - `DI` : 의존성 주입
  - `@Component`도 스프링 빈으로 자동 등록
    - 컴포넌트 스캔

  - 스프링 빈을 등록할 때, 기본으로 싱글톤 등록
    - 즉, 같은 스프링 빈이면 모두 같은 인스턴스

- **자바 코드로 직접 스프링 빈 등록하기**

  ```java
  // 예시
  
  @Configuration
  public class SpringConfig {
  
  	@Bean
  	public MemberService memberService() {
  		return new MemberService(memberRepository());
  	}
  }
  ```

  - 생성자 주입
    - 생성자 주입
      - 권장
    - 필드 주입
      - 필드에 `@Autowired` → 비추(바꿔치기 힘듦)
    - Setter 주입
      - setter메서드가 public하게 노출되는 단점
  - 장점
    - 예시로 리포지토리 교체시 return 객체만 변경하면 다른 로직 수정 필요 없음
  - 주의
    - `@Autowired`를 통한 `DI`는 `Controller`등과 같이 스프링이 관리하는 객체에서만 동작
      - 스프링 빈으로 등록하지 않고 직접 생성한 객체에서는 동작 X
      - 스프링 컨테이너에 올라가야 동작