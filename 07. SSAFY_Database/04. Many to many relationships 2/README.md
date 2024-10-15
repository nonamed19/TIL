### 프로필 페이지

- url 작성
    
    ```python
    # accounts/urls.py
    
    urlpatterns = [
    		...
        path('profile/<str:username>/', views.profile, name='profile'),
    ]
    ```
    
- view 함수 작성
    
    ```python
    # accounts/views.py
    
    def profile(request, username):
        # 어떤 유저의 프로필을 보여줄건지 유저를 조회(username을 사용해서 조회)
        User = get_user_model()
        person = User.objects.get(username=username)
        context = {
            'person': person,
        }
        return render(request, 'accounts/profile.html', context)
    ```
    
- profile 템플릿 작성
    
    ```python
    # accounts/profile.html
    
    <h1>{{ person.username }}의 프로필</h1>
    <hr>
    {% comment %} 유저가 작성한 게시글 {% endcomment %}
    <h1>{{ person.username }}가 작성한 게시글</h1>
    {% for article in person.article_set.all %}
      <p>{{ article.title }}</p>
    {% endfor %}
    
    {% comment %} 유저가 작성한 댓글 {% endcomment %}
    <h1>{{ person.username }}가 작성한 댓글</h1>
    {% for comment in person.comment_set.all %}
      <p>{{ comment.content }}</p>
    {% endfor %}
    
    {% comment %} 유저가 좋아요한 게시글 {% endcomment %}
    <h1>{{ person.username }}가 좋아요한 게시글</h1>
    {% for article in person.like_articles.all %}
      <p>{{ article.title }}</p>
    {% endfor %}
    ```
    
- 프로필 페이지로 이동할 수 있는 링크 작성
    
    ```python
    # articles/index.html
    
    <a href="{% url "accounts:profile" user.username %}">내 프로필</a>
    ```
    

### 모델 관계 설정

`ManyToManyField` 작성

```python
# accounts/models.py

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

참조 : 내가 팔로우하는 사람들 (팔로잉, `followings`)

역참조 : 상대방 입장에서 나는 팔로워 중 한 명 (팔로워, `followers`)

### 팔로잉 기능 구현

- url 작성
    
    ```python
    # accounts/urls.py
    
    urlpatterns = [
    		...
        path('<int:user_pk>/follow/', views.follow, name='follow'),
    ]
    ```
    
- view 함수 작성
    
    ```python
    # accounts/views.py
    
    @login_required
    def follow(request, user_pk):
        User = get_user_model()
        # 팔로우 요청을 보내는 대상
        you = User.objects.get(pk=user_pk)
        # 나 (팔로우 요청하는 사람)
        me = request.user
    
        # 나와 팔로우 대상자가 같지 않을 경우에만 진행 (다른 사람과만 팔로우 할 수 있음)
        if me != you:
            # 만약 내가 상대방의 팔로워 목록에 이미 있다면 팔로우 취소
            if me in you.followers.all():
                you.followers.remove(me)
                # me.followings.remove(you)
            else:
                you.followers.add(me)
            # me.followings.add(you)
        return redirect('accounts:profile', you.username)
    ```
    
- 프로필 유저의 팔로잉 관련 버튼 작성
    
    ```python
    # accounts/profile.html
    
    <div>
      팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
    </div>
    
    {% if request.user != person %}
      <div>
        <form action="{% url "accounts:follow" person.pk %}" method="POST">
          {% csrf_token %}
          {% if request.user in person.followers %}
            <input type="submit" value="언팔로우">
          {% else %}
            <input type="submit" value="팔로우">
          {% endif %}
        </form>
      </div>
    {% endif %}
    ```
    

### Fixtures

Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음

- Fixtures 파일을 직접 만들지 말 것 → 반드시 `dumpdata` 명령어를 사용하여 생성
- 데이터는 데이터베이스 구조에 맞추어 작성 되어있음
- 초기 데이터 제공

- `dumpdata` : 데이터베이스의 모든 데이터를 추출
    
    ```python
    $ python manage.py dumpdata [app_name[.ModelName] [app_name[.ModelName] ...]] > filename.json
    ```
    
    ```python
    # 적용 예시
    
    $ python manage.py dumpdata --indent 4 articles.article > articles.json
    $ python manage.py dumpdata --indent 4 articles.comment > comments.json
    $ python manage.py dumpdata --indent 4 accounts.user > users.json
    ```
    
- `loaddata` : Fixtures 데이터를 데이터베이스로 불러오기
    
    Fixtures 파일 기본 경로 : `app_name/fixtures`
    
    → Django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후 경로로 fixtures 파일을 찾아 load
    
    ```python
    # 적용 예시
    
    $ python manage.py loaddata articles.json users.json comments.json
    ```
    
    [`loaddata` 순서 주의사항]
    
    만약 `loaddata`를 한번에 실행하지 않고 별도로 실행한다면 모델 관계에 따라 load 순서가 중요할 수 있음
    
    - `comment`는 `article`에 대한 key 및 `user`에 대한 key가 필요
    - `article`은 `user`에 대한 key가 필요
    
    즉, 현재 모델 관계에서는 `user` → `article` → `comment` 순으로 data를 load해야 오류가 발생하지 않음
    

### Improve query

query 개선하기 : 같은 결과를 얻기 위해 DB 측에 보내는 query 개수를 점차 줄여 조회하기

- `annotate` :
    
    SQL의 GROUP BY를 사용
    
    쿼리셋의 각 객체에 계산된 필드를 추가
    
    집계 함수(`Count`, `Sum` 등)와 함께 자주 사용됨
    
    ```python
    Book.objects.annotate(num_authors=Count('authors'))
    ```
    
    - 의미
        
        결과 객체에 ‘num_authors’라는 새로운 필드를 추가
        
        이 필드는 각 책과 연관된 저자의 수를 계산
        
    - 결과
        
        결과에는 기존 필드와 함께 `‘num_authors’` 필드를 가지게 됨
        
        `book.num_authors`로 해당 책의 저자 수에 접근할 수 있게 됨
        
    - 문제 원인
        
        각 게시글마다 댓글 개수를 반복 평가
        
        ```python
        # index_1.html
        
        <p>댓글개수 : {{ article.comment_set.count }}</p>
        ```
        
    - 문제 해결
        
        게시글을 조회하면서 댓글 개수까지 한번에 조회해서 가져오기
        
        ```python
        # views.py
        
        def index_1(request):
            # articles = Article.objects.order_by('-pk')
            articles = Article.objects.annotate(Count('comment')).order_by('-pk')
            context = {
                'articles': articles,
            }
            return render(request, 'articles/index_1.html', context)
        ```
        
        ```python
        # index_1.html
        
        <p>댓글개수 : {{ article.comment__count }}</p>
        ```
        
- `select_related` :
    
    SQL의 `INNER JOIN`를 사용
    
    1:1 또는 N:1 참조 관계에서 사용; ForeinKey나 OneToOneField 관계에 대해 JOIN을 수행
    
    단일 쿼리로 관련 객체를 함께 가져와 성능을 향상
    
    ```python
    Book.objects.select_related('publisher')
    ```
    
    - 의미
        
        Book 모델과 연관된 Publisher 모델의 데이터를 함께 가져옴
        
        ForienKey 관계인 ‘publisher’를 JOIN하여 단일 쿼리만으로 데이터를 조회
        
    - 결과
        
        Book 객체를 조회할 때 연관된 Publisher 정보도 함께 로드
        
        `book.publisher.name`과 같은 접근이 추가적인 데이터베이스 쿼리 없이 가능
        
    - 문제 원인
        
        각 게시글마다 작성한 유저명까지 반복 평가
        
        ```python
        # index_2.html
        
        {% for article in articles %}
          <h3>작성자 : {{ article.user.username }}</h3>
          <p>제목 : {{ article.title }}</p>
          <hr>
        {% endfor %}
        ```
        
    - 문제 해결
        
        게시글을 조회하면서 유저 정보까지 한번에 조회해서 가져오기
        
        ```python
        # views.py
        
        def index_2(request):
            # articles = Article.objects.order_by('-pk')
            articles = Article.objects.select_related('user').order_by('-pk')
            context = {
                'articles': articles,
            }
            return render(request, 'articles/index_2.html', context)
        ```
        
- `prefetch_related` :
    
    SQL이 아닌 Python을 사용한 JOIN을 진행
    
    - 관련 객체들을 미리 가져와 메모리에 저장하여 성능을 향상
    
    M:N 또는 N:1 역참조 관계에서 사용
    
    - ManyToManyField나 역참조 관계에 대해 별도의 쿼리를 실행
    
    ```python
    Book.objects.prefetch_related('authors')
    ```
    
    - 의미
        
        Book과 Author는 ManyToMany 관계로 가정
        
        Book 모델과 연관된 모든 Author 모델의 데이터를 미리 가져옴
        
        Django가 별도의 쿼리로 Author 데이터를 가져와 관계를 설정
        
    - 결과
        
        Book 객체들을 조회한 후, 연관된 모든 Author 정보가 미리 로드됨
        
        `for author in book.authors.all()`와 같은 반복이 추가적인 데이터베이스 쿼리 없이 실행됨
        
    - 문제 원인
        
        각 게시글 출력 후 각 게시글의 댓글 목록까지 개별적으로 모두 평가
        
        ```python
        # index_3.html
        
        {% for article in articles %}
          <p>제목 : {{ article.title }}</p>
          <p>댓글 목록</p>
          {% for comment in article.comment_set.all %}
            <p>{{ comment.content }}</p>
          {% endfor %}
          <hr>
        {% endfor %}
        ```
        
    - 문제 해결
        
        게시글을 조회하면서 참조된 댓글까지 한번에 조회해서 가져오기
        
        ```python
        # views.py
        
        def index_3(request):
            # articles = Article.objects.order_by('-pk')
            articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
            context = {
                'articles': articles,
            }
            return render(request, 'articles/index_3.html', context)
        ```
        
- `select_related` & `prefetch_related` :
    - 문제 원인
        
        “게시글” + “각 게시글의 댓글 목록” + “댓글의 작성자”를 단계적으로 평가
        
        ```python
        # index_4.html
        
        {% for article in articles %}
          <p>제목 : {{ article.title }}</p>
          <p>댓글 목록</p>
          {% for comment in article.comment_set.all %}
            <p>{{ comment.user.username }} : {{ comment.content }}</p>
          {% endfor %}
          <hr>
        {% endfor %}
        ```
        
    - 문제 해결
        
        1단계 : 게시글을 조회하면서 참조된 댓글까지 한번에 조회
        
        ```python
        # views.py
        
        def index_4(request):
            # articles = Article.objects.order_by('-pk')
            articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
            # articles = Article.objects.prefetch_related(
            #     Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
            # ).order_by('-pk')
        
        ```
        
        2단계 : “게시글” + “각 게시글의 댓글 목록” + “댓글의 작성자”를 한번에 조회
        
        ```python
        # views.py
        
        def index_4(request):
            # articles = Article.objects.order_by('-pk')
            # articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
            articles = Article.objects.prefetch_related(
                Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
            ).order_by('-pk')
        ```
        

---

### 참고

### `‘.exists’` method

QuerySet에 결과가 하나 이상 존재하는지 여부를 확인하는 메서드

결과가 포함되어 있으면 True를 반환하고, 결과가 포함되어 있지 않으면 Fasle를 반환

데이터베이스에 최소한의 쿼리만 실행하여 효율적

전체 QuerySet을 평가하지 않고 결과의 존재 여부만 확인

→ 대량의 QuerySet에 있는 특정 객체 검색에 유용

```python
# articles/views.py

# 적용 전
if request.user in article.like_users.all():
	article.like_users.remove(request.user)

# 적용 후
if article.like_users.filter(pk=request.user.pk).exists():
	article.like_users.remove(request.user)

# 적용 전
if request.user in person.followers.all():
	person.followers.remove(request.user)

# 적용 후
if person.followers.filter(pk=request.user.pk).exists():
	person.followers.remove(request.user)
```

### 한꺼번에 dump 하기

```python
# 3개의 모델을 하나의 json 파일로
$ python manage.py dumpdata --indent 4 articles.article articles.comment accounts.user > data.json

# 모든 모델을 하나의 json 파일로
$ python manage.py dumpdata --indent 4 > data.json
```

### `loaddata` 인코딩 에러

[`loaddata` 시 encoding codec 관련 에러가 발생하는 경우]

- `dumpdata` 시 추가 옵션 작성
    
    ```python
    $ python -Xutf8 manage.py dumpdata [생략]
    ```
    
- 메모장 활용
    1. 메모장으로 `json` 파일 열기
    2. “다른 이름으로 저장” 클릭
    3. 인코딩을 `UTF8`로 선택 후 저장