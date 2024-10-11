### Web Application(web service) 개발 :

인터넷을 통해 사용자에게 제공되는 소프트웨어 프로그램을 구축하는 과정

다양한 디바이스(모바일, 태블릿, PC 등)에서 웹 브라우저를 통해 접근하고 사용할 수 있음

### 클라이언트와 서버

- 클라이언트(Client)
    
    서비스를 요청하는 주체(웹 사용자의 인터넷이 연결된 장치, 웹 브라우저)
    
- 서버(Server)
    
    클라이언트의 요청에 응답하는 주체(웹 페이지, 앱을 저장하는 컴퓨터)
    

[우리가 웹 페이지를 보게 되는 과정]

1. 웹 브라우저(클라이언트)에서 ‘google.com’을 입력 후 엔터

2. 웹 브라우저는 인터넷에 연결된 전 세계 어딘가에 있는 구글 컴퓨터(서버)에게 ‘메인 홈페이지.html’ 파일을 달라고 요청

3. 요청을 받은 구글 컴퓨터는 데이터베이스에서 ‘메인 홈페이지.html’ 파일을 찾아 응답

4. 웹 브라우저는 전달 받은 ‘메인 홈페이지.html’ 파일을 사람이 볼 수 있도록 해석해주고 사용자는 구글의 메인 페이지를 보게 됨

### Frontend & Backend :

- Frontend(프론트엔드)
    
    사용자 인터페이스(UI)를 구성하고, 사용자가 애플리케이션과 상호작용할 수 있도록 함
    
    ex. HTML, CSS, JavaScript, 프론트엔드 프레임워크 등
    
- Backend(백엔드)
    
    서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용 등을 담당
    
    ex. 서버 언어(Python, Java 등) 및 백엔드 프레임워크, 데이터베이스, API, 보안 등
    

### Web Framework :

웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구

(개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공)

### Django Framework :

Python 기반의 대표적인 웹 프레임워크

- 다양성
    
    Python 기반으로 웹, 모바일 앱 백엔드, API 서버 및 빅데이터 관리 등 광범위한 서비스 개발에 적합
    
- 확장성
    
    대량의 데이터에 대해 빠르고 유연하게 확장할 수 있는 기능을 제공
    
- 보안
    
    취약점으로부터 보호하는 보안 기능이 기본적으로 내장되어 있음
    
- 커뮤니티 지원
    
    개발자를 위한 지원, 문서 및 업데이트를 제공하는 활성화 된 커뮤니티
    

### 가상 환경 :

Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 독립적인 실행 환경

- 가상 환경 venv 생성
    
    `venv`라는 이름의 가상환경 생성
    
    임의 이름으로 생성이 가능하나 관례적으로 `venv` 이름을 사용
    
    ```python
    $ python -m venv venv
    ```
    
- 가상 환경 활성화
    
    활성어 명령어가 OS에 따라 다름에 주의
    
    ```python
    $ source venv/Scripts/activate
    ```
    
- 환경에 설치된 패키지 목록 확인
    
    ```python
    $ pip list
    ```
    
- 설치된 패키지 목록 생성
    
    현재 Python 환경에 설치된 모든 패키지와 그 버전을 텍스트 파일로 저장
    
    `requirements.txt` : 생성될 파일 이름(관례적으로 사용)
    
    ```python
    $ pip freeze > requirements.txt
    ```
    
- [번외] 패키지 목록 기반 설치
    
    생성된 `requirements.txt`로 다른 환경에서 동일한 환경 구성하기
    
    가상환경 활성화 후 `requirements.txt`에 작성된 목록을 기반으로 설치
    
    ```python
    $ pip install -r requirements.txt
    ```
    
- [번외] 가상환경 비활성화
    
    ```python
    $ deactivate
    ```
    

[가상환경 주의사항]

1. 가상 환경에 “들어가고 나오는” 것이 아니라 사용할 Python 환경을 “On/Off”로 전환하는 개념
    - 가상환경 활성화는 현재 터미널 환경에만 영향을 끼침
    - 새 터미널 창을 열면 다시 활성화해야 함
2. 가상환경은 “방”이 아니라 “도구 세트”
    - 활성화는 특정 도구 세트를 선택하는 것
3. 프로젝트마다 별도의 가상환경 사용
4. 일반적으로 가상환경 폴더 venv는 관련된 프로젝트와 동일한 경로에 위치
5. 가상환경 폴더 venv는 gitignore에 작성되어 원격 저장소에 공유되지 않음
    - 저장소 크기를 줄여 효율적인 협업과 배포를 가능하게 하기 위함(requirements.txt를 공유)

### 의존성 패키지 :

한 소프트웨어 패키지가 다른 패키지의 기능이나 코드를 사용하기 때문에 그 패키지가 존재해야만 제대로 작동하는 관계

사용하려는 패키지가 설치되지 않았거나, 호환되는 버전이 아니면 오류가 발생하거나 예상치 못한 동작을 보일 수 있음

개발환경에서는 각각의 프로젝트가 사용하는 패키지와 그 버전을 정확히 관리하는 것이 중요

[PROS]

- 가상환경의 패키지 목록을 쉽게 공유 가능
- 프로젝트의 의존성을 명확히 문서화
- 동일한 개발 환경을 다른 시스템에서 재현 가능

[CONS]

- 활성화된 가상환경에서 실행해야 정확한 패키지 목록 생성
- 시스템 전역 패키지와 구분 필요

### Django 프로젝트 :

[Django 프로젝트 생성 및 서버 실행]

- Django 프로젝트 생성
    
    `firstpjt`라는 이름의 프로젝트를 생성
    
    ```python
    $ django-admin startproject firstpjt .
    ```
    
- Django 서버 실행
    
    `manage.py`와 동일한 경로에서 진행
    
    ```python
    $ python manage.py runserver
    ```
    

### Django Design Pattern :

디자인 패턴 :

소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책

(공통적인 문제를 해결하는 데 쓰이는 형식화 된 관행)

→ “애플리케이션의 구조는 이렇게 구성하자”라는 관행

MVC(Model, View, Controller) 디자인 패턴 :

애플리케이션을 구조화하는 대표적인 패턴

(”데이터” & “사용자 인터페이스” & “비즈니스 로직”을 분리)

→ 시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지보수 할 수 있는 애플리케이션을 만들기 위해

MTV(Model, Template, View) 디자인 패턴 :

Django에서 애플리케이션을 구조화하는 패턴

(기존 MVC 패턴과 동일하나 단순히 명칭을 다르게 정의한 것)

### Project & Application :

Django Project :

애플리케이션의 집합 (DB 설정, URL 연결, 전체 앱 설정 등을 처리)

Django Application :

독립적으로 작동하는 기능 단위 모듈

(각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성)

[앱을 사용하기 위한 순서]

- 앱 생성
    
    앱의 이름은 ‘복수형’으로 지정하는 것을 권장
    
    ```python
    $ python manage.py startapp articles
    ```
    
- 앱 등록
    
    반드시 앱을 생성(1)한 후에 등록(2)해야 함
    
    (등록 후 생성은 불가능)
    
    ```python
    # Application definition
    
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```
    

[프로젝트 구조]

- settings.py
    
    프로젝트의 모든 설정을 관리
    
- urls.py
    
    요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결
    
- __init__.py
    
    해당 폴더를 패키지로 인식하도록 설정하는 파일
    
- asgi.py
    
    비동기식 웹 서버와의 연결 관련 설정
    
- wsgi.py
    
    웹 서버와의 연결 관련 설정
    
- manage.py
    
    Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티
    

[앱 구조]

- admin.py
    
    관리자용 페이지 설정
    
- models.py <MTV 패턴의 M>
    
    DB와 관련된 Model을 정의
    
- view.py <MTV 패턴의 V>
    
    HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환
    
    (url, model, template과 연계)
    
- apps.py
    
    앱의 정보가 작성된 곳
    
- tests.py
    
    프로젝트 테스트 코드를 작성하는 곳
    

### 요청과 응답 :

- URLs
    
    ```python
    from django.contrib import admin
    from django.urls import path
    # articles 앱의 views 함수 목록을 가져온다.
    # articles 패키지 안에 views 모듈을 가져온다.
    from articles import views
    
    urlpatterns = [
        # admin 이라는 주소로 요청이 들어오면,
        # admin 패키지 안에 site 모듈 안에 urls 함수를 호출
        path('admin/', admin.site.urls),
        path('index/', views.index)
    ]
    ```
    
    http://127.0.0.1:8000/index/로 요청이 왔을 때,
    
    `request` 객체를 `views` 모듈의 `index view` 함수에게 전달하며 호출
    
- View
    
    ```python
    from django.shortcuts import render
    
    # Create your views here.
    def index(request):
        # 페이지를 응답
        # return render(요청객체, 템플릿 경로)
        return render(request, 'index.html')
    ```
    
    view 함수가 정의되는 곳
    
    특정 경로에 있는 template과 request 객체를 결합해 응답 객체를 반환
    
    모든 view 함수는 첫번째 인자로 요청 객체를 필수적으로 받음
    
    매개변수 이름이 request가 아니어도 되지만 그렇게 작성하지 않음
    
- Template
    1. `articles` 앱 폴더 안에 `templates` 폴더 생성
        
        (폴더명은 반드시 `templates` 여야 하며, 개발자가 직접 생성해야 함)
        
    2. `templates` 폴더 안에 `articles` 폴더 생성
    3. `articles` 폴더 안에 템플릿 파일 생성
    
    app폴더 / templates / articles / index.html
    
    Django는 위의 지점까지 기본 경로로 인식하기 때문에 view 함수에서 template 경로 작성 시 이 지점 이후의 경로를 작성해야 함
    

---

### 가상환경 생성 루틴 :

1. 가상환경 생성
    
    ```python
    $ python -m venv venv
    ```
    
2. 가상환경 활성화
    
    ```python
    $ source venv/Scripts/activate
    ```
    
3. Django 설치
    
    ```python
    $ pip install django
    ```
    
4. 패키지 목록 파일 생성(패키지 설치시마다 진행)
    
    ```python
    $ pip freeze > requirements.txt
    ```
    
5. .gitignore 파일 생성 (첫 add 전)
6. git 저장소 생성(git init)
7. Django 프로젝트 생성

[가상환경을 사용하는 이유]

의존성 관리 : 라이브러리 및 패키지를 각 프로젝트마다 독립적으로 사용 가능

팀 프로젝트 협업 : 모든 팀원이 동일한 환경과 의존성 위에서 작업하며 버전 간 충돌을 방지

### Django 관련

LTS(Long-Term Support) :

프레임워크나 라이브러리 등 소프트웨어에서 장기간 지원되는 안정적인 버전을 의미할 때 사용

기업이나 대규모 프로젝트에서는 소프트웨어 업그레이드에 많은 비용과 시간이 필요하기 때문에 안정적이고 장기간 지원되는 버전이 필요

https://www.djangoproject.com/download

### `render` 함수 :

주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 `HttpResponse` 응답 객체를 반환하는 함수

```python
render(request, template_name, context)
```

1. `request` :
    - 응답을 생성하는 데 사용되는 요청 객체
2. `template_name` :
    - 템플릿 이름의 경로
3. `context` :
    - 템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)

### MTV 디자인 패턴 정리 :

- Model
    
    데이터와 관련된 로직을 관리
    
    응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
    
- Template
    
    레이아웃과 화면을 처리
    
    화면상의 사용자 인터페이스 구조와 레이아웃을 정의
    
- View
    
    Model & Template과 관련된 로직을 처리해서 응답을 반환
    
    클라이언트의 요청에 대해 처리를 분기하는 역할
    
- View 예시
    
    데이터가 필요하다면 model에 접근해서 데이터를 가져오고, 가져온 데이터를 template로 보내 화면을 구성하고, 구성된 화면을 응답으로 만들어 클라이언트에게 반환
    

### Trailing Comma(후행 쉼표) :

- Trailing Comma 정의
    
    리스트, 딕셔너리, 튜플 등의 자료구조에서 마지막 요소 뒤에 쉼표를 추가하는 것
    
    문법적으로 아무런 영향을 주지 않음
    
    일반적으로 선택 사항 (단일 요소 튜플을 만들 때는 예외)
    
- Trailing Comma 사용 이유
    
    새로운 요소를 추가하거나 순서를 변경할 때 편리
    
    값의 목록, 인자, 또는 import 항목들이 시간이 지남에 따라 확장될 것으로 예상되는 경우에 주로 사용
    
    여러 줄에 걸쳐 작성된 데이터 구조에서 유용하며, 코드의 가독성과 유지보수성을 향상시키는 데 도움
    
    일반적인 패턴은 각 값(등)을 별도의 줄에 배치하고, 항상 후행 쉼표를 추가한 뒤, 닫는 괄호/대괄호/중괄호를 다음 줄에 배치하는 것
    
    닫는 구분 기호와 같은 줄에 후행 쉼표를 두는 것은 권장하지 않음
    

### 프레임워크의 규칙 및 설계 철학 :

- Django 규칙
    
    `urls.py`에서 각 url 문자열 경로는 반드시 `‘/’`로 끝남
    
    `views.py`에서 모든 view 함수는 첫번째 인자로 요청 객체를 받음
    
    - 매개변수 이름은 반드시 `request`로 지정하기
    
    Django는 특정 경로에 있는 `template` 파일만 읽어올 수 있음
    
    - 특정 경로 : `app 폴더 / tempaltes /`
- 프레임워크 규칙
    
    프레임워크를 사용할 때는 일정한 규칙을 따라야 하며 이는 저마다의 설계 철학이나 목표를 반영하고 있음
    
    - 일관성 유지, 보안 강화, 유지보수성 향상, 최적화 등과 같은 이유
    
    프레임워크는 개발자에게 도움을 주는 도구와 환경을 제공하기 위해 규칙을 정해 놓은 것
    

https://docs.djangoproject.com/ko/4.2/misc/design-philosophies/