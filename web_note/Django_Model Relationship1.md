# Model Relationship1



### Foreign Key

- 참조하는 테이블에서 속성(필드)에 해당, 이는 참조되는 테이블의 기본 키를 가리킴
- 참조하는 테이블의 외래 키는 참조되는 테이블 행 1개에 대응
  - 참조되는 테이블에서 참조되는 테이블의 존재하지 않는 행을 참조할 수 없음
- 참조하는 테이블의 행 여러 개가 참조되는 테이블의 동일한 행을 참조할 수 없음

- 외래키의 값이 반드시 부모 테이블의 기본 키 x 유일한 값 o
- 참조 무결성
  - 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함



### ForeignKey field

- 2개의 위치 인자가 반드시 필요
  - 참조하는 model class
  - on_delete 옵션 : 외래 키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체 처리 방법
    - CASCADE
    - PROTECT
    - SET_NULL
    - SET_DEFAULT
    - SET() : ForeignKeyField 값을 SET에 설정된 함수 등에 의해 설정한다.
    - DO_NOTHING : 아무런 행동 x
    - RESTRICT
- migrate 작업 시 필드 이름에 _id를 추가하여 데이터베이스 열 이름 만듦
  - 참조하는 클래스 이름의 소문자로 작성하는 것이 바람직
- 데이터 무결성: 데이터의 정확성과 일관성을 유지하고 보증
  - 개체 무결성: PK는 고유한 값, NOT NULL
  - 참조 무결성: FK값이 DB의 특정 테이블의 PK값 참조
  - 범위(도메인) 무결성: 정의된 형식(범위)에서 RDB의 모든 컬럼 선언되도록 규정



### 1:N 관계 related manager

- 역참조('comment_set')
  - Article(1) -> Comment(N)
  - article.comment 형태로는 사용x, `article.comment_set manager`가 생성
  - Article 클래스에는 Comment와의 어떠한 관계도 작성 X
    - 게시글에 몇 개의 댓글이 작성 되었는지 Django ORM 보장 X
- 참조('article')
  - Comment(N) -> Article(1)
  - 댓글은 반드시 참조하는 게시글이 있으므로 comment.article과 같이 접근 가능
  - 실제 ForeignKeyField 또한 Comment 클래스에서 작성

- Foreignkey argumets - `related_name`
  - 역참조 시 사용할 이름을 변경할 수 있는 옵션
  - related_name = 'comments' 로 변경시
    - `article.comment_set`은 더이상 사용x `article.comments`





### Comment CREATE

- save(commit=False)
  - 아직 DB에 저장되지 않은 인스턴스 반환
  - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용



### Substituting a custom User model

#### User 모델 대체하기

- 내장 User 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있기 때문
- `AUTH_USER_MODEL` 값을 제공하여 default user model을 재정의 할 수 있도록 함
- 기본 사용자 모델이 충분하더라도 커스텀 유저 모델 설정하는 것을 권장

- AUTH_USER_MODEL
  - 프로젝트가 진행되는 동안 변경 x
  - 프로젝트 시작 시 설정, 참조하는 모델은 첫번째 마이그레이션에서 사용 가능해야 함
  - 기본값 : `auth.User`(auth 앱의 User모델)
    - settings.py에서 앱.User로 바꿔주자



### Custom user & Bulit-in auth forms

- 기존 User 모델을 사용하기 때문에 커스텀 User 모델로 다시 작성하거나 확장해야 하는 forms

  - UserCreationForm
  - UserChangeForm

- get_user_model()

  - 현재 프로젝트에서 활성화된 사용자 모델 반환
    - 커스터마이징한 상황에서는 Custom User모델을 반환
  - User 클래스를 직접 참조하는 대신 `django.contrib.auth,get_user_model()`을 사용하여 참조해야 한다고 강조

  

### User - Article (1:N)

- User 모델 참조하기
  - `settings.AUTH_USER_MODEL`
    - User 모델에 대한 외래 키 또는 다대다 관계를 정의 할 때 사용
    - models.py에서 User모델을 참조할 때 사용
    - 리턴 문자열
  - `get_user_model()`
    - models.py 가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용
    - 리턴 오브젝트
- User와 Article 간 모델 관계 정의 후 migration
  - 1 enter
    - 현재 화면에서 기본 값을 설정하겠다
    - `값` enter : 기존 테이블에 추가되는 user_id의 필드의 값을 `값` 으로 설정
  - 2 enter
- 게시글 출력 필드 수정
  - NOT NULL : `form.save(commit=False)` , `앱.user = request.user`
  - 