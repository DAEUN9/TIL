## 예외 처리와 오류 페이지



- 서블릿 예외 처리 - 시작
  - 예외 처리 방법
    - `Exception` (예외)
    - `response.sendError` (HTTP 상태 코드, 오류 메시지)



- Exception(예외)
  - 웹 애플리케이션
    - `WAS`(여기까지 전파) <- `필터` <- `서블릿` <- `인터셉터` <- `컨트롤러`(예외발생)
      - 만약 애플리케이션에서 예외를 잡지 못하고, 서블릿 밖까지 예외가 전달되면
      - 톰캣 같은 `WAS` 까지 예외 전달
      - 서버 내부에서 처리할 수 없는 오류가 발생한 것으로 생각해서 `HTTP 500` 호출 



- response.sendError(HTTP 상태 코드, 오류 메시지)
  - 당장 예외가 발생하는 것은 아니지만
  - 서블릿 컨테이너에게 오류가 발생했다는 점을 전달할 수 있다.
  - `response.sendError(HTTP 상태 코드)`
  - `response.sendError(HTTP 상태 코드, 오류 메시지)`
  - `sendError` 흐름
    - `WAS`(`sendError` 호출 기록 확인) <- `필터` <- `서블릿` <- `인터셉터` <- `컨트롤러 `(`response.sendError()`)
    - 호출시 response 내부에는 오류가 발생했다는 상태를 저장
    - 서블릿 컨테이너는 고객에게 응답 전에 `response` 에 `sendError()` 가 호출되었는지 확인
    - 호출되었다면 설정한 오류 코드에 맞추어 기본 오류 페이지를 보여준다



- 서블릿 예외 처리 - 오류 화면 제공

  ```java
  // hello/exception/WebServerCustomizer
  
  @Component
  public class WebServerCustomizer implements WebServerFactoryCustomizer<ConfigurableWebServerFactory> {
  
      @Override
      public void customize(ConfigurableWebServerFactory factory) {
  
          ErrorPage errorPage404 = new ErrorPage(HttpStatus.NOT_FOUND, "/error-page/404");
          ErrorPage errorPage500 = new ErrorPage(HttpStatus.INTERNAL_SERVER_ERROR, "/error-page/500");
          ErrorPage errorPageEx = new ErrorPage(RuntimeException.class, "/error-page/500");
  
          factory.addErrorPages(errorPage404, errorPage500, errorPageEx);
      }
  }
  ```

  - `response.sendError(404)` : `errorPage404 ` 호출
  - `response.sendError(500)` : `errorPage500` 호출
  - `RuntimeException` 또는 그 자식 타입의 예외: `errorPageEx` 호출



- 서블릿 예외 처리 - 오류 페이지 작동 원리

  - 예외가 `WAS`까지 전달되면 오류 페이지 정보를 확인

  - 오류 페이지를 출력하기 위해 오류 페이지 경로 다시 요청

  - 예외 발생과 오류 페이지 요청 흐름

    ```
    1. WAS(여기까지 전파) <- 필터 <- 서블릿 <- 인터셉터 <- 컨트롤러(예외발생)
    
    2. WAS `/error-page/500` 다시 요청 -> 필터 -> 서블릿 -> 인터셉터 -> 컨트롤러(/error-page/500) -> View
    ```

  - **중요한 점은 웹 브라우저(클라이언트)는 서버 내부에서 이런 일이 일어나는지 전혀 모른다는 점**

  - 오직 서버 내부에서 오류 페이지를 찾기 위해 추가적인 호출

  - 오류 정보 추가

    - `WAS`는 오류 페이지를 단순히 다시 요청만 하는 것이 아니라
    - 오류 정보를 `request`의 `attribute`에 추가해서 넘겨줌

  - `request.attribute`에 서버가 담아준 정보

    - `javax.servlet.error.exception` : 예외
    - `javax.servlet.error.exception_type` : 예외 타입
    - `javax.servlet.error.message` : 오류 메시지
      - `ex`의 경우 `NestedServletException` 스프링이 한번 감싸서 반환
    - `javax.servlet.error.request_uri` : 클라이언트 요청 URI
    - `javax.servlet.error.servlet_name` : 오류가 발생한 서블릿 이름 
    - `javax.servlet.error.status_code` : HTTP 상태 코드



- 서블릿 예외 처리 - 필터

  - 예외 발생과 오류 페이지 요청 흐름

    ```
    1. WAS(여기까지 전파) <- 필터 <- 서블릿 <- 인터셉터 <- 컨트롤러(예외발생)
    
    2. WAS `/error-page/500` 다시 요청 -> 필터 -> 서블릿 -> 인터셉터 -> 컨트롤러(/error-page/500) -> View
    ```

    - 필터, 인터셉터가 중복 호출되면 비효율적
    - 클라이언트로 부터 발생한 정상 요청인지, 아니면 오류 페이지를 출력하기 위한 내부 요청인지 구분할 수 있어야 한다
      - `DispatcherType` 이라는 추가 정보를 제공

  - `javax.servlet.DispatcherType`

    ```java
    public enum DispatcherType {
        FORWARD, // MVC에서 배웠던 서블릿에서 다른 서블릿이나 JSP를 호출할 때
        INCLUDE, // 서블릿에서 다른 서블릿이나 JSP의 결과를 포함할 때
        REQUEST, // 고객이 처음 요청
        ASYNC, // 서블릿 비동기 호출
        ERROR // 오류 요청
    }
    ```

    - `request.getDispatcherType()`

  ```java
  @Configuration
  public class WebConfig implements WebMvcConfigurer {
      @Bean
      public FilterRegistrationBean logFilter() {
  
          FilterRegistrationBean<Filter> filterRegistrationBean = new FilterRegistrationBean<>();
  
          filterRegistrationBean.setFilter(new LogFilter());
          filterRegistrationBean.setOrder(1);
          filterRegistrationBean.addUrlPatterns("/*");
          filterRegistrationBean.setDispatcherTypes(
                  DispatcherType.REQUEST,
                  DispatcherType.ERROR);
          
          return filterRegistrationBean;
      }
  }
  ```

  - 기본 값이 `DispatcherType.REQUEST` 이므로 오류 처리에 크게 영향 없음
  - `filterRegistrationBean.setDispatcherTypes(DispatcherType.REQUEST, DispatcherType.ERROR);`
    - 클라이언트 요청은 물론이고, 오류 페이지 요청에서도 필터가 호출



- 서블릿 예외 처리 - 인터셉터

  - 필터의 경우

    - 필터를 등록할 때 어떤 `DispatcherType` 인 경우에 필터를 적용할 지 선택할 수 있었다

  - 인터셉터의 경우

    - 인터셉터는 서블릿이 제공하는 기능이 아니라 스프링이 제공하는 기능
    - `DispatcherType` 과 무관하게 항상 호출
    - 오류 페이지 경로를 `excludePathPatterns` 를 사용해서 빼주면 된다

    ```java
    // webConfig
    
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        
        registry.addInterceptor(new LogInterceptor())
            .order(1)
            .addPathPatterns("/**")
            .excludePathPatterns(
                "/css/**", "/*.ico"
                , "/error", "/error-page/**" //오류 페이지 경로
        	);
    }
    ```

    

- 전체 흐름

  - `/hello` 정상 요청

    ```
    WAS(/hello, dispatchType=REQUEST) -> 필터 -> 서블릿 -> 인터셉터 -> 컨트롤러 -> View
    ```

  - `/error-ex` 오류 요청

    - 필터는 `DispatchType` 으로 중복 호출 제거 ( `dispatchType=REQUEST` )
    - 인터셉터는 경로 정보로 중복 호출 제거( `excludePathPatterns("/error-page/**")` )

    ```
    1. WAS(/error-ex, dispatchType=REQUEST) -> 필터 -> 서블릿 -> 인터셉터 -> 컨트롤러
    2. WAS(여기까지 전파) <- 필터 <- 서블릿 <- 인터셉터 <- 컨트롤러(예외발생)
    3. WAS 오류 페이지 확인
    4. WAS(/error-page/500, dispatchType=ERROR) -> 필터(x) -> 서블릿 -> 인터셉터(x)
     	-> 컨트롤러(/error-page/500) -> View
    ```




- 스프링 부트 - 오류 페이지1
  - 스프링 부트는 예외 처리 페이지 자동 등록
    - `ErrorPage` 를 자동으로 등록한다. 이때 `/error` 라는 경로로 기본 오류 페이지를 설정
    - 상태코드와 예외를 설정하지 않으면 기본 오류 페이지로 사용
  - `BasicErrorController` 라는 스프링 컨트롤러를 자동으로 등록
    - `ErrorPage` 에서 등록한 `/error` 를 매핑해서 처리하는 컨트롤
  - 참고
    - `ErrorMvcAutoConfiguration` 이라는 클래스가 오류 페이지를 자동으로 등록하는 역할
  - 개발자는 오류 페이지만 등록
    - `BasicErrorController` 는 기본적인 로직이 모두 개발되어 있음
    - 오류 페이지 화면만 `BasicErrorController` 가 제공하는 룰과 우선순위에 따라서 등록
  - 뷰 선택 우선순위 - `BasicErrorController`의 처리 순서
    1. 뷰 템플릿
       - `resources/templates/error/500.html`
       - `resources/templates/error/5xx.html`
    2. 정적 리소스( `static` , `public `)
       - `resources/static/error/400.html`
       - `resources/static/error/404.html`
       - `resources/static/error/4xx.html`
    3. 적용 대상이 없을 때 뷰 이름( `error` )
       - `resources/templates/error.html`



- 스프링 부트 - 오류 페이지2

  - `BasicErrorController`가 제공하는 기본 정보들

    - 다음 정보를 model에 담아서 뷰에 전달

    ```
    * timestamp: Fri Feb 05 00:00:00 KST 2021
    * status: 400
    * error: Bad Request
    * exception: org.springframework.validation.BindException
    * trace: 예외 trace
    * message: Validation failed for object='data'. Error count: 1
    * errors: Errors(BindingResult)
    * path: 클라이언트 요청 경로 (`/hello`)
    ```

  - `BasicErrorController`에서 오류 정보를 model에 포함할지 여부

    - 오류 내부 정보들을 고객에게 노출하는 것은 좋지 않다
      - 고객 혼란, 보안상 문제

    - `application.properties`

      ```
      server.error.include-exception=false : exception 포함 여부( true , false )
      server.error.include-message=never : message 포함 여부
      server.error.include-stacktrace=never : trace 포함 여부
      server.error.include-binding-errors=never : errors 포함 여부
      ```

      - 3가지 옵션
        - `never` : 사용하지 않음
        - `always` :항상 사용
        - `on_param` : 파라미터가 있을 때 사용
          - 파라미터가 있으면 해당 정보 model에 담겨서 노출
          - 디버그 시 문제 확인 사용, 운영 서버에는 권장X
          - `message=&errors=&trace=` 추가하면 다 보임

  - 사용자에게는 간단한 오류 메시지만 보여주고 오류는 서버에 로그로 확인하자



- 스프링 부트 오류 관련 옵션
  - `server.error.whitelabel.enabled=true` : 오류 처리 화면을 못 찾을 시, 스프링 `whitelabel` 오류 페이지 적용할지
  - `server.error.path=/error` : 오류 페이지 경로
    - 스프링이 자동 등록하는 서블릿 글로벌 오류 페이지 경로와 `BasicErrorController` 오류 컨트롤러 경로에 함께 사용된다
    - 보통 기본값을 사용하긴 함



- 확장 포인트
  - 에러 공통 처리 컨트롤러의 기능을 변경하고 싶으면
    - `ErrorController` 인터페이스를 상속 받아서 구현
    - `BasicErrorController` 상속 받아서 기능을 추가
