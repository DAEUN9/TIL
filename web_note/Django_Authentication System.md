### Authentication System

- `django.contrib.auth` : 인증 프레임워크의 핵심과 기본 모델을 포함
- `django.contrib.contenttypes` : 사용자가 생성한 모델과 권한 연결



### 쿠키

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE 형식으로 저장
- 요청한 웹페이지 받으며 쿠키 함께 저장하고 같은 서버 재 요청시 쿠키도 함께 전송

- 목적

  - 세션 관리
  - 개인화
  - 트래킹

- 수명(lifetime)

  - Session cookies

    - 현재 세션 종료되면 삭제
    - 브라우저가 현재 세션이 종료되는 시기 정의

  - Persistent cookies(or Permanent cookies)

    - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간 지나면 삭제

      



### 세션

- 사이트와 특정 브라우저 사이의 상태 유지

- 서버 접속하면 `session id` 발급, 쿠키에 저장

  다시 접송하면 저장된 쿠키 전달(쿠키와 함께 전달)

- Djnago의 세션

  - 미들웨어 통해 구현

  - database-backed sessions 저장 방식 기본 값 사용

  - 세션 정보는 Django DB의 `django_session` 테이블에 저장

    

### Authentication System in MIDDLEWARE

- `SessionMiddleware` : 요청 전반에 걸쳐 세션 관리
- `AuthenticationMiddleware` : 세션을 사용하여 사용자를 요청과 연결



### 로그인

#### AuthenticationForm

- 로그인을 위한 form
- request를 첫번째 인자로 취함



#### login(request, user, backend=None)

- 현재 세션에 연결하려는 인증 된 사용자가 있는 경우 login() 함수 필요
- HttpRequest 객체와 User 객체 필요
- 세션에 user의 ID 저장(== 로그인)
- 로그인 후 브라우저와 Django DB에서 `sessionid` 확인



#### get_user()

- AuthenticationForm 의 인스턴스 메서드

- user_cashe는 인스턴스 생성시에 None으로 할당

  유효성 검사를 통과했을 경우 로그인 한 사용자 객체로 할당

- 인스턴스의 유효성 먼저 확인, 유효할때만 user를 제공



### Authentication data in templates

#### context processors

- 템플릿이 렌더링 될 때 자동으로 호출 가능한 컨텍스트 데이터
- 작성된 프로세서는 RequestContext에서 사용 가능한 변수로 포함





#### Users

- 현재 로그인한 사용자를 나타내는 auth.User 인스턴스( 로그인안하면 AnonymousUser)
- `{{ user }}`에 저장



### 로그아웃

#### logout(request)

- HttpRequest 객체를 인자로 받고 반환 값 없음

- 사용자가 로그인하지 않은 경우 오류 발생 x

- 현재 요청에 대한 session date를 DB, 클라이언트의 쿠키에서 sessionid 완전삭제\

  -> 이전 사용자의 세션 데이터에 엑세스 하는 것 방지



### 로그인 사용자에 대한 접근 제한

1. `is_authenticated` attribute

   - 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성

     (AnonymousUser에 대해서는 항상 False)

   - 권한과 관련 없음, 사용자 활성화 상태나 세션 유효성 확인 x

2. `login_required` decorator

   - 로그인되어 있지 않으면, 