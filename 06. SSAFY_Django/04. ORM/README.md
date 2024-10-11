ORM(Object-Relational-Mapping) :

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

### QuerySet API :

`Article.objects.all()`

Model class

Manager

Queryset API

ORM에서 데이터를 검색, 필터링, 정렬 및 정렬 및 그룹화 하는 데 사용하는 도구

→ API를 활용하여 SQL이 아닌 Python 코드로 데이터를 처리

python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것

CRUD :

소프트웨어가 가지는 기본적인 데이터 처리 기능

- Create (저장)
- Read (조회)
- Update (갱신)
- Delete (삭제)

Query :

데이터베이스에 특정한 데이터를 보여 달라는 요청

파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달

QuerySet :

데이터베이스에게서 전달 받은 객체 목록(데이터 모음)

→ 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음

Django ORM을 통해 만들어진 자료형

단, 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

### Create :

- 외부 라이브러리 설치 및 설정
    
    ```python
    $ pip install ipython
    $ pip install django-extensions
    ```
    
- application 등록 : ‘django_extensions’
- requirements.txt 업데이트
    
    ```python
    $ pip freeze > requirements.txt
    ```
    
- 4. Django shell 실행
    
    ```python
    $ python manage.py shell_plus
    ```
    

Django shell :

Django 환경 안에서 실행되는 python shell

(입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미침)

데이터 객체를 만드는(생성하는) 3가지 방법

- 특정 테이블에 새로운 행을 추가하여 데이터 추가
    
    ```python
    # Article(class)로부터 article(instance) 생성
    In [1]: article = Article()
    
    In [2]: article
    Out[2]: <Article: Article object (None)>
    
    In [3]: article.title = 'first' # 인스턴스 변수(title)에 값을 할당
    In [4]: article.content = 'django!' # 인스턴스 변수(content)에 값을 할당
    
    # 인스턴스 article을 활용하여 인스턴스 변수 활용하기
    In [5]: article.title
    Out[5]: 'first'
    
    In [6]: article.content
    Out[6]: 'django!'
    
    # save를 하지 않으면 아직 DB에 값이 저장되지 않음
    In [7]: Article.objects.all()
    Out[7]: <QuerySet []>
    
    In [8]: article.save()
    
    In [9]: Article.objects.all()
    Out[9]: <QuerySet [<Article: Article object (1)>]>
    ```
    
- 새로운 행을 추가하며 instance에 데이터 초기값을 입력
    
    ```python
    In [10]: article = Article(title='second', content='django!')
    
    # save를 하지 않으면 아직 DB에 값이 저장되지 않음
    In [11]: article
    Out[11]: <Article: Article object (None)>
    
    In [16]: article.save()
    
    In [17]: article
    Out[17]: <Article: Article object (2)>
    
    # QuerySet에 Article object (2) 게시글이 추가됨을 확인할 수 있음
    In [18]: Article.objects.all()
    Out[18]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
    ```
    
- QuerySet API 중 `create()` 메서드 활용
    
    ```python
    # 위 2가지 방법과 달리 바로 저장 이후 바로 생성된 데이터가 반환된다.
    In [19]: Article.objects.create(title='third', content='django!')
    Out[19]: <Article: Article object (3)>
    ```
    

`save()` : 객체를 데이터베이스에 저장하는 인스턴스 메서드

### Read :

Return new QuerySets(복수 개체)

- `all()` : 전체 데이터 조회
    
    ```python
    In [20]: Article.objects.all()
    Out[20]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
    ```
    
- `filter()` : 주어진 매개변수와 일치하는 객체를 포함하는 QuerySet 반환
    
    ```python
    In [21]: Article.objects.filter(content='django!')
    Out[21]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
    
    In [22]: Article.objects.filter(title='first')
    Out[22]: <QuerySet [<Article: Article object (1)>]>
    
    In [23]: Article.objects.filter(title='abc')
    Out[23]: <QuerySet []>
    ```
    

Do not return QuerySets(단일 개체)

- `get()` : 주어진 매개변수와 일치하는 객체를 반환
    
    객체를 찾을 수 없으면 `DoesNotExist` 예외를 발생시키고, 둘 이상의 객체를 찾으면 `MultipleObjectsReturned` 예외를 발생시킴
    
    위와 같은 특징을 가지고 있기 때문에 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함
    
    ```python
    In [24]: Article.objects.get(pk=1)
    Out[24]: <Article: Article object (1)>
    
    In [25]: Article.objects.get(pk=100)
    DoesNotExist: Article matching query does not exist.
    
    In [26]: Article.objects.get(content='django!')
    MultipleObjectsReturned: get() returned more than one Article -- it returned 3!
    ```
    

### Update :

인스턴스 변수를 변경 후 `save` 메서드 호출

```python
# 수정할 인스턴스 조회
In [36]: article = Article.objects.get(pk=2)

# 인스턴스 변수를 변경
In [39]: article.content = 'ssafy!!!!!'

# 저장
In [42]: article.save()

# 정상적으로 변경된 것을 확인
In [41]: article.content
Out[41]: 'ssafy!!!!!'
```

### Delete :

삭제하려는 데이터 조회 후 `delete` 메서드 호출

```python
# 삭제할 인스턴스 조회
In [43]: article = Article.objects.get(pk=2)

# delete 메서드 호출 (삭제 된 객체가 반환)
In [44]: article.delete()
Out[44]: (1, {'articles.Article': 1})

# 삭제한 데이터는 더이상 조회할 수 없음
In [45]: article.objects.get(pk=2)
AttributeError: Manager isn't accessible via Article instances
```

### ORM with view :

### 전체 게시글 조회 :

- 전체 게시글 조회
- 단일 게시글 조회(향후 학습 예정)

---

https://docs.djangoproject.com/en/5.1/ref/models/querysets/

https://docs.djangoproject.com/en/5.1/topics/db/queries/

- Field lookups :
    
    Query에서 조건을 구성하는 방법
    
    QuerySet 메서드 `filter()`, `exclude()` 및 `get()`에 대한 키워드 인자로 지정됨
    
    ```python
    # Field lookups 예시
    
    # 내용에 'dja'가 포함된 모든 게시글 조회
    Article.objects.filter(content__contains='dja')
    
    # 내용이 'he'로 시작하는 모든 게시글 조회
    Article.objects.filter(title__startswith='he')
    ```
    

ORM, QuerySet API를 사용하는 이유 :

1. 데이터베이스 추상화
    
    개발자는 특정 데이터베이스 시스템에 종속되지 않고 일관된 방식으로 데이터를 다룰 수 있음
    
2. 생산성 향상
    
    복잡한 SQL 쿼리를 직접 작성하는 대신 Python 코드로 데이터베이스 작업을 수행할 수 있음
    
3. 객체 지향적 접근
    
    데이터베이스 테이블을 Python 객체로 다룰 수 있어 객체 지향 프로그래밍의 이점을 활용할 수 있음