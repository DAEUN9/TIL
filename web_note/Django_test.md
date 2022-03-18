# Django 정리(for test)

> 실습 내용 따로 살펴보기

DB 안나옴



##### Django1

- 요청과 응답
- Template
- HTML Form
- URL



#### static vs Dynamic 웹 페이지

- `static`
  - 서버에 미리 저장된 파일 사용자에게 그대로 전달
  - 요청에 대한 추가적인 처리 과정 x 응답 보냄
  - 모든 상황 모든 사용자 동일
  - html, css, javascript 로 주로 작성
  - flat page라고도 함
- `dynamic`
  - 요청에 대해 추가적인 처리 과정 이후 응답 보냄
  - 방문자에 따라 페이지 내용 다름
  - 서버 사이드 프로그래밍 언어(python, java, c++ 등) 사용. 상호작용

#### Framework

- 특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
- Application framework 라고도 함
- 재사용할 수 있는 수많은 코드를 프레임워크로 통합
- `web framework` : 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적



### ❗MTV Pattern

- `Model`
  - 응용 프로그램의 데이터 구조를 정의 DB의 기록을 관리(추가, 수정 삭제)

- `Template`

  - 파일을 구조나 레이아웃 정의
  - 실제 내용을 보여주는 데 사용

- `View`

  - http 요청을 수신하고 http 응답을 반환
  - model을 통해 요청을 충족시키는데 필요한 데이터에 접근
  - template에게 응답의 서식 설정을 맡김

  

**MVC <-> MTV** ❗

| MVC Pattern    | MTV(Django)  |
| -------------- | ------------ |
| **M**odel      | **M**odel    |
| **V**iew       | **T**emplate |
| **C**ontroller | **V**iew     |



### Django 시작하기

- 프로젝트 생성
  - `django-admin startproject <프로젝트명> .`
  - `.` : 현재 디렉토리 의미❗

- Django 서버 시작(활성화)
  - `python manage.py runserver`



### 프로젝트 구조

> 각각 어떤 것을 위한 파일인지

- `settings.py`
  - 애플리케이션의 모든 설정을 포함
- `url.py`
  - 사이트의 url과 적절한 views의 연결 지정
- `manage.py`
  - 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
    - `python manage.py <command> [options]`
  - 프로젝트 폴더 밖에 생성



### Application 생성

- 복수형 이름 권장

### Application 구조

- `admin.py`
  - 관리자용 페이지를 설정
- `apps.py`
  - 앱의 정보 작성
- `models.py`
  - 앱에서 사용하는 Model 정의

- `tests.py`
  - 프로젝트의 테스트 코드 작성
- `views.py`
  - view 함수들 정의
  - HTTP 요청을 수신하고 응답 반환
  - Model을 통해 요청에 맞는 필요 데이터에 접근
  - Template에게 HTTP응답 서식 맡김
- `urls.py`
  - **자동생성 X**❗
  - HTTP 요청을 알맞은 view로 전달



### Project & Application

- `project` : Application의 집합
  - 앱은 여러 프로젝트에 있을 수 있음

- `Application` : 실제 요청을 처리하고 페이지를 부여줌
  - 하나의 역할 및 기능 단위



### 앱 등록

- 반드시 앱 생성 후, `settings.py`의 `INSTALLED_APPS`에 앱 추가



### Templates

- 실제 내용을 보여주는데 사용
- 파일 구조나 레이아웃 정의
- Template 파일 경로 기본 값은 **app 폴더 안의 templates 폴더**로 지정



### 추가 설정

- `LANGUAGE_CODE`
  - 번역, `USE_I18N` 활성화되어 있어야 함❗
  - 한국은 `ko-kr`
- `TIME_ZONE`
  - 데이터베이스 연결의 시간대를 나타내는 문자열 지정

```
- USE_I18N : 번역 시스템 활성화 여부 지정
- USE_L10N : local 형식을 기본적으로 활성화할지 여부 지정
- USE_TZ : datetimes가 기본적으로 시간대를 인식하는지 여부 지정
```



### ❗DTL(Django Template Language)

**Built-in tag**

- [for](https://docs.djangoproject.com/ko/3.2/ref/templates/builtins/#for)

​	ex)

```django
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
</ul>
```

- | Variable              | Description                                                  |
  | --------------------- | ------------------------------------------------------------ |
  | `forloop.counter`     | The current iteration of the loop (1-indexed)                |
  | `forloop.counter0`    | The current iteration of the loop (0-indexed)                |
  | `forloop.revcounter`  | The number of iterations from the end of the loop (1-indexed) |
  | `forloop.revcounter0` | The number of iterations from the end of the loop (0-indexed) |
  | `forloop.first`       | True if this is the first time through the loop              |
  | `forloop.last`        | True if this is the last time through the loop               |
  | `forloop.parentloop`  | For nested loops, this is the loop surrounding the current one |

  - for ... empty
    - `empty`: 비었을 때나 찾을 수 없을 때 보여줌

  ex)

```django
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>Sorry, no athletes in this list.</li>
{% endfor %}
</ul>
```

- if

- load
  - 커스텀 템플릿 태그세트를 로드
  - 여러개 등록 가능

​	ex)

```django
{% load somelibrary package.otherlibrary %}
```

- url
  - 절대 경로 참조
  - `urls.py`에서 설정한 `name` 활용

​	ex)

```django
{% url 'some-url-name' v1 v2 %} 
```



**Built-in filter**

- [date](https://docs.djangoproject.com/ko/3.2/ref/templates/builtins/#date)

  - format

  | Format character | Description                                    | Example output   |
  | ---------------- | ---------------------------------------------- | ---------------- |
  | **Day**          |                                                |                  |
  | `d`              | Day of the month, 2 digits with leading zeros. | `'01'` to `'31'` |
  | `j`              | Day of the month without leading zeros.        | `'1'` to `'31'`  |
  | `D`              | Day of the week, textual, 3 letters.           | `'Fri'`          |
  | **Month**        |                                                |                  |
  | `m`              | Month, 2 digits with leading zeros.            | `'01'` to `'12'` |
  | `n`              | Month without leading zeros.                   | `'1'` to `'12'`  |
  | `M`              | Month, textual, 3 letters.                     | `'Jan'`          |
  | **Year**         |                                                |                  |
  | `y`              | Year, 2 digits with leading zeros.             | `'00'` to `'99'` |
  | `Y`              | Year, 4 digits.                                | `'1999'`         |
  | **Time**         |                                                |                  |
  | `h`              | Hour, 12-hour format.                          | `'01'` to `'12'` |
  | `H`              | Hour, 24-hour format.                          | `'00'` to `'23'` |
  | `i`              | Minutes.                                       | `'00'` to `'59'` |
  | `s`              | Seconds, 2 digits with leading zeros.          | `'00'` to `'59'` |

​	ex)

```django
{{ value|date:"D d M Y" }}
```

- length

  ex)

```django
{{ value|length }}
```

- lower/upper

​	ex)

```django
{{ value|lower }}
{{ value|upper }}
```



### DTL Syntax

- variable : `{{ variable }}`
  - views.py 에서 정의한 변수 사용
  - render()의 세 번째 인자로, 딕셔너리 형태의 key가 변수명이 됨

- filters : `{{ variable|filter }}`
- tags : `{% tag %}`
  - 반복 또는 논리 수행
  - 일부 태그는 시작과 종료 태그 필요



### Templat inheritance

- extends : `{% extends ''%}`
  - 반드시 템플릿 최상단 작성
  - 자식이 부모 템플릿 확장(상속)
- block : `{% block content %} {% endblock %}`
  - 자식 템플릿이 채울 수 있는 공간
    