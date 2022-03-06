[toc]

# Django 시작하기

## 1. 가상환경 설정하기

1. 가상환경 만들기
   * `python -m venv venv`
2. 가상환경 활성화 하기
   * `source venv/Scripts/activate`

3. 가상환경이 정상적으로 실행되었는지 확인한다.
   * `pip list` 
   * 방금 생성되었고 정상적인 상태라면 pip list에는 2개 (pip, setuptools)만 있다.



## 2. Django 설치하기

#### requirements.txt가 없는 경우

1. 장고 3.2 버전 설치하기
   * `pip install django==3.2`

2. 설치된 장고를 패키지 리스트로 만들기
   * `pip freeze > requirements.txt`



#### requirements.txt가 있는 경우

1. requirements.txt 를 이용하여 패키지를 설치
   * `pip install -r requirements.txt`



## 3. Django 프로젝트 생성

1. 장고 프로젝트를 생성

   * 프로젝트 폴더를 미리 생성하여 내부에 manage.py 파일을 만들고 싶을 때
     * `django-admin startproject 프로젝트명 .`

   * 폴더를 생성하고 싶은 경우
     * `django-admin startproject 프로젝트명`

2. `manage.py` 위치 확인

   * `ls` 명령어를 이용하여 `manage.py` 의 존재 여부를 확인하고 없다면 해당 파일이 있는 곳으로 이동한다



## 4. Django Application 생성

1. 어플리케이션을 생성
   * `python manage.py startapp 어플리케이션명`
2. 어플리케이션을 `settings.py`에 등록
   * `INSTALLED_APP` 에 생성한 어플리케이션을 등록한다.
   * 이 때 콤마를 빠뜨리지 않도록 한다. 



## 5. url 분리

1. `settings.py` 와 같은 곳에 위치한 `urls.py`를 먼저 수정

   * 주석을 확인하여 `include` 를 import 한다.
   * urlpatterns 리스트에 
     * `path('경로/', include('앱이름.urls')),` 를 추가한다.
     * 경로는 보통 앱이름으로 작성

2. 만든 앱 폴더 내부에 `urls.py` 파일을 새로 생성한다.

   * 기본 구조를 다음과 같이 작성한다.

     ```python
     from django.urls import path
     from . import views
     
     app_name = '앱이름'
     urlpatterns = [
         
     ]
     ```



## 6. base.html 

1. 공통으로 사용하는 템플릿 파일을 만든다.

   * 위치는 `manage.py`와 같은 곳에 `templates` 라는 폴더를 생성
   * 생성한 `templates` 폴더 내부에 `base.html` 파일 생성

2. 위에서 생성한 `templates` 폴더의 위치를 `settings.py`에 등록

   * 아래와 같이 DIRS 에 `BASE_DIR / 'templates'` 를 리스트 내부에 추가

   ```python
   TEMPLATES = [
       {
           ...
           'DIRS': [BASE_DIR / 'templates'],
   		...
       }
   ]
   ```

3. base.html 을 작성한다.

   * DTL) block tag 반드시 추가한다.

     ```html
     <body>
         {% block content %}
         {% endblock content %}
     </body>
     ```

     * block 위치에 다른 template 들이 위치하게 됨





---

**이후 urls.py -> views.py -> template(html) 작성 순서로 개발을 하면 됩니다.**



여기까지가 최소한의 프로젝트를 생성하고 공통적으로 반드시 해야 될 내용입니다.

곧 알고리즘 후반기 교육기간이기 때문에 많이들 잊을거라 따로 정리해드려요. 

