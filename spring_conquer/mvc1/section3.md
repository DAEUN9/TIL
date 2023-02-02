## 서블릿, JSP, MVC 패턴

```java
// 회원 저장소

/**
 * 동시성 문제가 고려되어 있지 않음, 실무에서는 ConcurrentHashMap, AtomicLong 사용 고려
 Thread-safe로 구현되어 멀티쓰레드에서 synchronized 없이 사용할 수 있음. 또한 synchronized 보다 적은 비용으로 동시성을 보장
 
 ConcurrentHashMap: ConcurrentHashMap은 버킷 단위로 lock을 사용하기 때문에 같은 버킷만 아니라면 Lock을 기다릴 필요가 없다는 특징이 있습니다.(버킷당 하나의 Lock을 가지고 있다
 */
public class MemberRepository {
     private static Map<Long, Member> store = new HashMap<>(); //static 사용
     private static long sequence = 0L; //static 사용
     private static final MemberRepository instance = new MemberRepository();
     public static MemberRepository getInstance() {
     	return instance;
     }
     private MemberRepository() {
     }
     public Member save(Member member) {
         member.setId(++sequence);
         store.put(member.getId(), member);
         return member;
     }
     public Member findById(Long id) {
    	 return store.get(id);
     }
     public List<Member> findAll() {
     	return new ArrayList<>(store.values());
     }
     public void clearStore() {
     	store.clear();
     }
}
```

- 템플릿 엔진
  - HTML 문서에서 필요한 곳만 코드를 적용해서 동적으로 변경 가능
    - `JSP`, `Thymeleaf`, `Freemarker`, `Velocity`



- JSP로 회원 관리 웹 애플리케이션 만들기

  - `<%@ page contentType="text/html;charset=UTF-8" language="java" %>`
    -  JSP 문서는 이렇게 시작해야 한다.

  - JSP는 서버 내부에서 서블릿으로 변환

  - `<%@ page import="hello.servlet.domain.member.MemberRepository" %>`
    -  자바의 import 문과 같다.
  - `<% ~~ %>` 이 부분에는 자바 코드를 입력할 수 있다. 
  - `<%= ~~ %>` 이 부분에는 자바 코드를 출력할 수 있다.
  - 서블릿과 JSP의 한계
    - JAVA 코드, 리포지토리 등 다양한 코드가 JSP에 노출
    - JSP의 역할이 너무 많음
    - 변경의 라이프 사이클이 달라서 유지보수가 좋지 않음
      - ex) UI 일부 로직 수정, 비즈니스 로직 수정



- MVC 패턴의 - 개요
  - 컨트롤러
    - HTTP 요청을 받아서 파라미터를 검증하고, 비즈니스 로직을 실행한다. 그리고 뷰에 전달할 결과 데이터를 조회해서 모델에 담는다.
  - 모델
    - 뷰에 출력할 데이터를 담아둔다. 뷰가 필요한 데이터를 모두 모델에 담아서 전달해주는 덕분에 뷰는 비즈니스 로직이나 데이터 접근을 몰라도 되고, 화면을 렌더링 하는 일에 집중할 수 있다.
  - 뷰
    - 모델에 담겨있는 데이터를 사용해서 화면을 그리는 일에 집중한다. 여기서는 HTML을 생성하는 부분을 말한다
  - 일반적으로 비즈니스 로직은 서비스에서 처리, 컨트롤러는 서비스를 호출하는 역할



- MVC 패턴 - 적용

  - `dispatcher.forward()` : 다른 서블릿이나 JSP로 이동할 수 있는 기능, 서버 내부에서 다시 호출 발생
  - `redirect` vs `forwrd`
    - 리다이렉트는 클라이언트에 응답이 나갔다가 클라이언트가 다시 요청
      - 클라이언트가 인지하고 URL 경로도 변경
    - 포워드는 서버 내부에서 일어남
      - 클라이언트가 인지 못함
  - JSP 에서 상대 경로를 유지해 주어야 함
  - `request.setAttribute()` : request 객체에 데이터를 보관해서 뷰에 전달 가능
  - `request.getAttribute()` : 데이터를 꺼냄
  - `${}` 문법을 통해 데이터를 편리하게 조회 가능

  ```jsp
  // 회원 목록 조회 뷰
  
  <%@ page contentType="text/html;charset=UTF-8" language="java" %>
  <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
  <html>
  <head>
   <meta charset="UTF-8">
   <title>Title</title>
  </head>
  <body>
  <a href="/index.html">메인</a>
  <table>
   <thead>
   <th>id</th>
   <th>username</th>
   <th>age</th>
   </thead>
   <tbody>
   <c:forEach var="item" items="${members}">
   <tr>
   <td>${item.id}</td>
   <td>${item.username}</td>
   <td>${item.age}</td>
   </tr>
   </c:forEach>
   </tbody>
  </table>
  </body>
  </html>
  ```

  - `<c:forEach>` 사용을 위해 `<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>` 선언 필요
  - JSP와 같은 뷰 템플릿은 화면을 렌더링 하는데 특화된 다양한 기능 제공



- MVC 패턴 - 한계

  - 포워드 중복

    - View로 이동하는 코드가 항상 중복 호출, 이 부분을 메서드로 공통화해도 되지만, 해당 메서드도 항상 직접 호출 필요

    ```java
    RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);
    dispatcher.forward(request, response);
    ```

    - ViewPath에 중복
      - 만약 jsp가 아닌 다른 뷰로 변경한다면 전체 코드 다 변경 필요

    ```java
    String viewPath = "/WEB-INF/views/new-form.jsp";
    
    // prefix : /WEB-INF/views/
    // suffix : .jsp
    ```

    - 사용하지 않는 코드
      - `HttpServletRequest`, `HttpServletResponse`를 사용하는 코드는 테스트 케이스를 작성하기도 어려움
    - 공통 처리가 어렵다
      - 컨트롤러 호출 전에 공통 기능 처리 필요(수문장 역할)
      - **프론트 컨트롤러** 패턴을 도입하자