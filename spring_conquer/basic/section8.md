## 빈 생명주기 콜백

- **빈 생명주기 콜백 시작**

  - DB 커넥션 풀이나, 네트워크 소켓처럼 애플리케이션 시작 시점에 필요한 연결을 미리 해두고, 애플리케이션 종료 시점에 연결을 모두 종료하는 작업을 진행하려면, 객체의 초기화와 종료 작업 필요

  - 스프링 빈의 라이프 사이클

    - **객체 생성 -> 의존관계 주입**

  - 초기화 작업은 의존관계 주입이 모두 완료되고 난 다음에 호출해야 함

  - 스프링 빈의 이벤트 라이프 사이클

    - **스프링 컨테이너 생성 -> 스프링 빈 생성 -> 의존관계 주입 -> 초기화 콜백 -> 사용 -> 소멸전 콜백 -> 스프링 종료**

  - `초기화 콜백` : 빈이 생성되고, 빈의 의존관계 주입이 완료된 후 호출

  - `소멸전 콜백` : 빈이 소멸되기 직전 호출

  - 객체의 생성과 초기화를 분리하자

    - 생성자는 파라미터를 받고, 메모리를 할당해서 객체를 생성하는 책임을 가짐
    - 초기화는 생성된 값들을 활용해 외부 커넥션을 연결하는 등 무거운 동작 수행
    - 생성자 안에서 무거운 초기화 작업을 수행하는 것 보다 명확하게 나누는 것이 유지보수 관점에서 좋음
    - 초기화 작업이 내부 값들만 약간 변경하는 단순한 작업이면 생성자에서 한번에 처리하는게 나을 수도 있음

  - **빈 생명주기 콜백 지원 방법**

    1. 인터페이스(`InitializingBean`, `DisposableBean`)
    2. 빈 등록 초기화, 소멸 메서드
    3. 애노테이션(`@PostConstruct`, `@PreDestroy`)

    

- **인터페이스 InitializingBean, DisposableBean**

  ```java
  import org.springframework.beans.factory.DisposableBean;
  import org.springframework.beans.factory.InitializingBean;
  
  public class NetworkClient implements InitializingBean, DisposableBean {
      private String url;
      
      // 빈 의존관계 주입 후 콜백
      @Override
      public void afterPropertiesSet() throws Exception {
          connect();
      }
      
      // 빈 소멸 직전 콜백
      @Override
      public void destroy() throws Exception {
          disconnect();
      }
      
      // connect()와 disconnect() 생략
  }
  ```

  - 단점
    - 코드가 스프링 전용 인터페이스에 의존하게 됨
    - 초기화, 소멸 메서드의 이름을 변경할 수 없음
    - 내가 코드를 고칠 수 없는 외부 라이브러리에 적용할 수 없음

  

- **빈 등록 초기화, 소멸 메서드**

  - 초기화, 소멸 메서드 지정
  - ex) `Bean(initMethod = "init", destroyMethod = "close")`
  - 설정 정보 사용 특징
    - 메서드 이름을 자유롭게 줄 수 있음
    - 스프링 빈이 스프링 코드에 의존하지 않음
    - 코드가 아니라 설정 정보를 사용하기 때문에 코드를 고칠 수 없는 외부 라이브러리에도 적용할 수 있음
  - 종료 메서드 추론
    - 라이브러리는 대부분 `close`, `shutdown` 이라는 이름의 종료 메서드 사용
    - `@Bean`의 `destroyMethod`는 기본값이 `(inferred)`(추론)으로 등록
    - 이 추론 기능은 `close`, `shutdown`라는 이름의 메서드를 자동으로 호출
    - 추론 기능을 사용하기 싫으면 `destroyMethod=""` 처럼 빈 공백 지정

  

- **애노테이션 @PostConstruct, @PreDestroy**

  - 특징
    - 최신 스프링에서 가장 권장하는 방법
    - 애노테이션을 하나만 붙이면 되므로 매우 편리
    - 패키지가 `javax.annotation.PostConstruct`임, 스프링에 종속적이지 않고 `JSR-250`이라는 자바 표준
      - 스프링이 아닌 다른 컨테이너에서도 동작
    - 컴포넌트 스캔과 잘 어울림 `@Bean` 뿐만 아니라 `@Component`에서도 사용
    - 단점은 외부 라이브러리에는 적용 불가

  ```java
  import javax.annotation.PostConstruct;
  import javax.annotation.PreDestroy;
  
  public class NetworkClient {
      private String url;
      
      // 빈 의존관계 주입 후 콜백
      @PostConstruct
      public void init() {
          connect();
      }
      
      // 빈 소멸 직전 콜백
      @PreDestroy
      public void close() {
          disconnect();
      }
      
      // connect()와 disconnect() 생략
  }
  ```

  

