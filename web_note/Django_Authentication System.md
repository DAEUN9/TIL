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

   - 로그인되어 있지 않으면, `settings.LOGIN_URL`에 설정된 문자열 기반 절대 경로로 redirect
     - LOGIN_URL의 기본 값은 '/accounts/login/'
   - 인증 성공 시 사용자가 redirect 되어야 하는 경로는 `next`라는 쿼리 문자열 매개 변수에 저장
     - 예시 `/accounts/login/?next=/articles/create/`

- `next` query string parameter
  - 정상 로그인시 redirect를 위해 주소를 keep
  - 단, 별도로 처리 해주지 않으면 view에 설정한 redirect 경로로 이동
  - 현재 URL로(next parameter가 있는) 요청을 보내기 위해 action 값 비우기
- 두 데코레이터로 인해 발생하는 구조적 문제와 해결
  - `@require_POST` 와 `@login_required`를 함께 사용하면 에러 발생
    - `405(Method Not Allowed)` status code
  - 로그인 성공 후 next에 담긴 경로로 리다이렉트 될 때 에러 발생
  - 두가지 문제 발생
    - redirect 과정에서 POST 데이터 손실
    - redirect 요청은 POST 방식이 불가능하기 때문에 GET 방식으로 요청





### 회원가입

#### UserCreationForm

- 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm
- 3개의 필드를 가짐
  - username(from the user model)
  - password1
  - password2





### 회원탈퇴



### 회원정보 수정

#### UserChangeForm

- 사용자의정보 및 권한을 변경하기 위해 admin 인터페이스에 사용되는 ModelForm
- 문제점
  - 일반 사용자가 접근해서는 안될 정보들(fields)까지 모두 수정이 가능
  - 따라서 `UserChangeForm`을 상속받아 `CustomUserChangeForm`이라는 서브클래스를 작성해 접근 가능한 필드 조정



#### get_user_model()

- 현재 프로젝트에서 활성화된 사용자 모델 반환

- Django는 User 클래스를 직접 참조하는 대신 `django.contirb.auth.get_user_model()`을 사용하여 참조해야 함

  

### 비밀번호 변경

#### PasswordChangeForm

- 이전 비밀번호를 입력하여 비밀번호 변경
- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스



#### 암호 변경 시 세션 무효화 방지

- `update_session_auth_hash(request, user)`
  - 현재 요청과 새 session hash가 파생 될 업데이트 된 사용자 객체를 가져오고, session hash 적절하게 업데이트
  - 비밀번호가 변경되면 기존 세션과의 회원 인증 정보고 일치하게 되어 로그인 상태를 유지할 수 없기 때문
  - 암호가 변경되어도 로그아웃되지 않도록 새로운 password hash로 session  업데이트