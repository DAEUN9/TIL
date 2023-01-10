## 스프링 웹 개발 기초

- 정적 컨텐츠

  - 파일을 그대로 클라이언트에 내려주는 방식
  - 스프링 부트에서 기본적으로 지원함
  - 파이프라인
    1. `localhost:8080/hello-static.html` 을 요청하고 내장 톰켓 서버 거침
    2. 스프링 컨테이너에서 관련 컨트롤러 탐색
    3. (없으면) `hello-static.html` 파일을 탐색
    4. 웹 브라우저로 내려줌

- MVC와 템플릿 엔진

  - MVC : Model, View, Controller

  - 파이프라인

    1. `localhost:8080/hello-mvc` 을 요청하고 내장 톰켓 서버 거침

    2. 스프링 컨테이너에서 `helloController` 매핑

       `hello-template` 리턴하여 스프링으로 넘겨줌

    3. `viewResolver`가 `Thymeleaf` 에게 `templates/hello-template.html`를 찾아서 넘겨줌

    4. `Thymeleaf`가 렌더링해서 변환한 html을 웹브라우저에 넘겨줌

  - 정적 컨텐츠와 차이점

    - html변환 여부에 차이가 있음

- **API**

  - json 데이터 포맷 방식으로 데이터를 클라이언트에 보냄

  - 파이프라인

    1. `localhost:8080/hello-api` 을 요청하고 내장 톰켓 서버 거침

       1. 스프링 컨테이너에서 `helloController` 매핑

       `@ResponseBody` 를 사용, 객체를 HTTP BODY에 문자 내용을 직접 리턴

       1. `HttpMessageConverter` 동작

       기본 문자 처리 : `StringHttpMessageConverter`

       기본 객체 처리 : `MappingJackson2HttpMessageConverter`

       1. json 형태로 웹브라우저에 데이터를 넘겨줌