## 로그인 처리1 - 쿠키, 세션



- 패키지 구조 설계

  ```
  package 구조
  hello.login
  	domain
  		item
  		member
  		login
  	web
  		item
  		member
  		login
  ```

  - 도메인
    - 화면, UI, 기술 인프라 등등의 영역은 제외한 시스템이 구현해야 하는 핵심 비즈니스 업무 영역을 말함
  - 향후 web을 다른 기술로 바꾸어도 도메인은 그대로 유지할 수 있어야 한다.
  - web은 domain을 알고있지만 domain은 web을 모르도록 설계
  - web은 domain을 의존하지만, domain은 web을 의존하지 않는다



- 로그인 처리하기 - 쿠키 사용

  - 쿠키에 시간 정보를 주지 않으면 세션 쿠키

    - 브라우저 종료시 쿠키 모두 종료

  - 쿠키 생성 로직

    ```java
    Cookie idCookie = new Cookie("memberId", String.valueOf(loginMember.getId()));
    response.addCookie(idCookie);
    ```

    - 웹 브라우저는 종료 전까지 회원의 `id`를 서버에 계속 보내 줄 것

  - 쿠키 만료 시키기

    ```java
    @PostMapping("/logout")
    public String logout(HttpServletResponse response) {
        expireCookie(response, "memberId");
        return "redirect:/";
    }
    
    private void expireCookie(HttpServletResponse response, String cookieName) {
        Cookie cookie = new Cookie(cookieName, null);
        cookie.setMaxAge(0);
        response.addCookie(cookie);
    }
    ```

    

- 쿠키와 보안 문제
  - 쿠키 값은 임의로 변경될 수 있음
    - 클라이언트가 쿠키를 강제로 변경하면 다른 사용자가 된다
    - 실제 웹브라우저 개발자모드 -> Application -> Cookie 변경으로 확인
    - `Cookie: memberId=1` -> `Cookie: memberId=2` (다른 사용자의 이름이 보임)
  - 쿠키에 보관된 정보는 훔쳐갈 수 있음
    - 이 정보가 웹 브라우저에도 보관되고, 네트워크 요청마다 계속 클라이언트에서 서버로 전달된다.
    - 쿠키의 정보가 나의 로컬 PC에서 털릴 수도 있고, 네트워크 전송 구간에서 털릴 수도 있다.
  - 대안
    - 쿠키에서는 중요한 값 노출 X
    - 사용자 별로 예측 불가능한 임의의 토큰(랜덤)을 노출함
    - 서버에서는 토큰과 사용자 id를 매핑해서 인식하고 서버에서 토큰 관리
    - 토큰을 털어가도 시간이 지나면 사용할 수 없도록 서버에서 해당 토큰의 만료시간을 짧게 유지
    - 해킹이 의심되는 경우 서버에서 해당 토큰을 강제로 제거



- 로그인 처리하기 - 세션 동작 방식

  - 세션
    - 중요한 정보를 모두 서버에 저장
    - 클라이언트와 서버는 추정 불가능한 임의의 식별자( ex) `UUID` ) 값으로 연결
    - 생성된 세션 ID와 세션에 보관할 값( `memberA` )을 서버의 세션 저장소에 보관
    - 서버는 클라이언트에 `mySessionId` 라는 이름으로 세션ID 만 쿠키에 담아서 전달한다
    - 클라이언트는 쿠키 저장소에 `mySessionId` 쿠키를 보관
    - 서버에서는 클라이언트가 전달한 쿠키 정보로 세션 저장소 조회

  - 보안 문제 해결

    - 쿠키 값을 변조 가능 -> 예상 불가능한 복잡한 세션Id를 사용한다.
    - 쿠키에 보관하는 정보는 클라이언트 해킹시 털릴 가능성이 있다.  -> 세션Id가 털려도 여기에는 중요한 정보가 없다.

    - 쿠키 탈취 후 사용 -> 해커가 토큰을 털어가도 시간이 지나면 사용할 수 없도록 서버에서 세션의 만료시간을 짧게(예: 30분) 유지한다
    - 또는 해킹이 의심되는 경우 서버에서 해당 세션을 강제로 제거하면 된다.



- 로그인 처리하기 - 세션 직접 만들기
  - 세션 생성
    - sessionId 생성 (임의의 추정 불가능한 랜덤 값)
    - 세션 저장소에 sessionId와 보관할 값 저장
    - sessionId로 응답 쿠키를 생성해서 클라이언트에 전달
  - 세션 조회
    - 클라이언트가 요청한 sessionId 쿠키의 값으로, 세션 저장소에 보관한 값 조회
  - 세션 만료
    - 클라이언트가 요청한 sessionId 쿠키의 값으로, 세션 저장소에 보관한 sessionId와 값 제거
  - 서블릿에서 세션 기능 제공
    - 밑에서 확인 해보자



- 로그인 처리하기 - 서블릿 HTTP 세션1

  - `HttpSession`

    - 직접 만든 `SessionManager`와 같은 방식으로 동작
    - `JSESSIONID` 라는 쿠키 생성

  - Controller 일부 로직

    ```java
    //세션이 있으면 있는 세션 반환, 없으면 신규 세션 생성
    HttpSession session = request.getSession(); // 디폴트가 true(없으면 생성)
    // false면 기존 객체는 찾지만 새로 생성X
    
    //세션에 로그인 회원 정보 보관
    session.setAttribute(SessionConst.LOGIN_MEMBER, loginMember);
    ```

  - `session.invalidate()` : 세션을 제거한다
  - `session.getAttribute(SessionConst.LOGIN_MEMBER)` : 로그인 시점에 세션에 보관한 회원 객체를 찾는다



- 로그인 처리하기 - 서블릿 HTTP 세션2

  - `@SessionAttribute`

    - 세션에서 attribute를 한번에 꺼냄
    - `@SessionAttribute(name = "loginMember", required = false) Member loginMember`
    - 세션을 생성하지는 않음

  - TrackingModes

    - 로그인을 처음 시작하면 URL에 `jsessionid` 포함

      - `http://localhost:8080/;jsessionid=F59911518B921DF62D09F0DF8F83F872`

    - 웹 브라우저가 쿠키를 지원하지 않을 때 쿠키 대신 URL로 세션 유지하는 방법

    - 타임리프 같은 템플릿은 엔진을 통해서 링크를 걸면 `jsessionid` 를 URL에 자동으로 포함

    - 웹 브라우저가 쿠키를 지원하는지 하지 않는지 최초에는 판단하지 못하므로, 쿠키 값도 전달하고, URL에 `jsessionid` 도 함께 전달

    - 항상 쿠키를 통해서만 세션을 유지하고 싶으면 다음 옵션을 넣어주면 된다

      ```
      // application.properties
      
      server.servlet.session.tracking-modes=cookie
      ```

      

- 세션 정보

  - 세션 정보 컨트롤러

    ```java
    @GetMapping("/session-info")
    public String sessionInfo(HttpServletRequest request) {
    
        HttpSession session = request.getSession(false);
        if (session == null) {
            return "세션이 없습니다.";
        }
    
        //세션 데이터 출력
        session.getAttributeNames().asIterator()
            .forEachRemaining(name -> log.info("session name={}, value={}",
                                               name, session.getAttribute(name)));
    
        log.info("sessionId={}", session.getId());
        log.info("maxInactiveInterval={}", session.getMaxInactiveInterval());
        log.info("creationTime={}", new Date(session.getCreationTime()));
        log.info("lastAccessedTime={}", new Date(session.getLastAccessedTime()));
        log.info("isNew={}", session.isNew());
    
        return "세션 출력";
    }
    ```

    - `sessionId` : 세션Id, `JSESSIONID` 의 값이다.
      - 예) `34B14F008AA3527C9F8ED620EFD7A4E1`
    - `maxInactiveInterval` : 세션의 유효 시간
      - 예) 1800초, (30분)
    - `creationTime` : 세션 생성일시
    - `lastAccessedTime` : 세션과 연결된 사용자가 최근에 서버에 접근한 시간
      - 클라이언트에서 서버로 `sessionId` ( `JSESSIONID` )를 요청한 경우에 갱신된다
    - `isNew` : 새로 생성된 세션인지, 아니면 이미 과거에 만들어졌고, 클라이언트에서 서버로 `sessionId` ( `JSESSIONID` )를 요청해서 조회된 세션인지 여부



- 세션 타임아웃 설정

  - 세션을 무한정 보관하면 발생하는 문제

    - 세션은 로그아웃을 직접 호출하는 경우 삭제되지만, 브라우저 창을 닫으면 사용자가 웹 브라우저를 종류한 것인지 인식할 수 없음
      - HTTP는 비 연결성이므로
      - 서버에서 세션 데이터를 언제 삭제해야 하는지 판단 어려움
    - 세션과 관련된 쿠키( `JSESSIONID` )를 탈취 당했을 경우 오랜 시간이 지나도 해당 쿠키로 악의적인 요청을 할 수 있다.
    - 세션은 기본적으로 메모리에 생성된다. 메모리의 크기가 무한하지 않기 때문에 꼭 필요한 경우만 생성해서 사용해야 한다

  - 세션의 종료 시점

    - 사용자가 서버에 최근에 요청한 시간을 기준으로 30분(임의) 정도를 유지해주는 것
    - `HttpSession` 은 이 방식을 사용

  - 스프링 부트로 글로벌 설정

    ```
    // application.properties
    
    server.servlet.session.timeout=60
    ```

    -  60초, 기본은 1800(30분)
    - 글로벌 설정은 분 단위로 설정해야 한다. 60(1분), 120(2분), ...)

  - 세션 타임아웃 발생

    - `LastAccessedTime` 이후로 `timeout` 시간이 지나면, `WAS`가 내부에서 해당 세션을 제거한다.

  - 주의

    - 세션에는 최소한의 데이터만 보관해야 한다는 점
    - 보관한 데이터 용량 * 사용자 수로 세션의 메모리 사용량이 급격하게 늘어나서 장애로 이어질 수 있다
    - 세션의 시간을 너무 길게 가져가면 메모리 사용이 계속 누적 될 수 있으므로 적당한 시간을 선택하는 것이 필요