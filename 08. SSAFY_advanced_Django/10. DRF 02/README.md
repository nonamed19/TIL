### DRF with N:1 Relation

[URL과 HTTP requests methods 설계]

|  | GET | POST | PUT | DELETE |
| --- | --- | --- | --- | --- |
| `comments/` | 댓글 목록 조회 |  |  |  |
| `comments/1/` | 단일 댓글 조회 |  | 단일 댓글 수정 | 단일 댓글 삭제 |
| `articles/1/comments` |  | 댓글 생성 |  |  |
- GET method - 조회(List)
    - 댓글 목록 조회를 위한 `CommentSerializer` 정의
    
    ```python
    # articles/serializers.py
    
    from .models import Article, Comment
    
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'
    ```
    
    - url 작성
    
    ```python
    # articles/urls.py
    
    urlpatterns = [
    		...
        path('comments/', views.comment_list),
    ]
    ```
    
    - view 함수 작성
    
    ```python
    # articles/views.py
    
    from .models import Article, Comment
    from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
    
    @api_view(['GET'])
    def comment_list(request):
        # 댓글 전체 조회
        comments = Comment.objects.all()
        # 댓글 목록 쿼리셋을 직렬화 진행
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    ```
    
- GET method - 조회(Detail)
    - url 작성
    
    ```python
    # articles/urls.py
    
    urlpatterns = [
    		...
        path('comments/<int:comment_pk>/', views.comment_detail),
    ]
    ```
    
    - view 함수 작성
    
    ```python
    # articles/views.py
    
    @api_view(['GET'])
    def comment_detail(request, comment_pk):
        # 단일 댓글 조회
        comment = Comment.objects.get(pk=comment_pk)
        # 단일 댓글 직렬화
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    ```
    
- POST method - 생성
    - url 작성
    
    ```python
    # articles/urls.py
    
    urlpatterns = [
    		...
        path('articles/<int:article_pk>/comments/', views.comment_create),
    ]
    
    ```
    
    - view 함수 작성
    
    ```python
    # articles/views.py
    
    @api_view(['POST'])
    def comment_create(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        serializer = CommentSerializer(data=request.data)
    
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    ```
    
    `save()` 메서드는 특정 `Serializer` 인스턴스를 저장하는 과정에서 추가 데이터를 받을 수 있음
    
    - `article` field를 읽기 전용 필드로 설정
    
    ```python
    # articles/serializers.py
    
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'
            read_only_fields = ('article',)
    ```
    
    읽기 전용 필드(`read_only_fields`) :
    
    데이터를 전송 받은 시점에 “유효성 검사에서 제외시키고, 데이터 조회 시에는 출력”하는 필드
    
- DELETE method - 삭제
    - view 함수 작성
    
    ```python
    # articles/views.py
    
    @api_view(['GET', 'DELETE'])
    def comment_detail(request, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        if request.method == 'GET':
            ...
    
        elif request.method == 'DELETE':
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    ```
    
- PUT method - 수정
    - view 함수 작성
    
    ```python
    # articles/views.py
    
    @api_view(['GET', 'DELETE', 'PUT'])
    def comment_detail(request, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        if request.method == 'GET':
    				...
        
        elif request.method == 'DELETE':
    				...
    
        elif request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    ```
    

### 응답 데이터 재구성

※ 댓글 조회 시 게시글 번호만 제공해주는 것이 아닌 ‘게시글의 제목’까지 제공하기

필요한 데이터를 만들기 위한 Serializer는 내부에서 추가 선언이 가능

```python
# articles/serializers.py

class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    # 기존 article 데이터 값을 override
    # 그런데 기존 필드를 override 하게되면 Meta클래스의 read_only_fields를 사용할 수 없음
    # 모델 시리얼라이저의 read_only 인자 값으로 재설정
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        # fields에 작성된 필드는 모두 유효성 검사 목록에 포함됨
        fields = '__all__'
        # 외래 키 필드를 "읽기전용 필드"로 지정
        # 이유는? 외래 키 데이터는
        # 1. 유효성 검사에서는 제외
        # 2. 결과 데이터에는 포함하고 싶음.
        # read_only_fields = ('article',)
```

### 역참조 데이터 구성

Article → Comment 간 역참조 관계를 활용한 JSON 데이터 재구성

- 단일 게시글 조회 시 해당 게시글에 작성된 댓글 목록도 함께 붙여서 응답
- 단일 게시글 조회 시 해당 게시글에 작성된 댓글 개수도 함께 붙여서 응답

### 단일 게시글 + 댓글 목록

`Nested relationship(역참조 매니저 활용)`

- 모델 관계 상으로 참조하는 대상은 참조되는 대상의 표현에 포함되거나 중첩될 수 있음
- 이러한 중첩 관계는 serializers를 필드로 사용하여 표현 가능

```python
# articles/serializers.py

class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)

    # comment_set 역참조 데이터를 override
    comment_set = CommentDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = '__all__'
```

### 단일 게시글 + 댓글 개수

- 댓글 개수에 해당하는 새로운 필드 생성

```python
# articles/serializers.py

class ArticleSerializer(serializers.ModelSerializer):
		...
    comment_set = CommentDetailSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
```

`‘source’` arguments

- 필드를 채우는 데 사용할 속성의 이름
- 점 표기법(dotted notation)을 사용하여 속성을 탐색 할 수 있음

※ 읽기 전용 필드 지정 이슈 ※

- 특정 필드를 override 혹은 추가한 경우 `read_only_fields`는 동작하지 않음
- 이런 경우 새로운 필드에 read_only 키워드 인자로 작성해야 함

```python
# articles/serializers.py

class ArticleSerializer(serializers.ModelSerializer):
		...
    comment_set = CommentDetailSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('comment_set', 'comment_count',)
```

### 읽기 전용 필드

- 사용자에게 입력으로는 받지 않지만 제공은 해야 하는 경우
- 새로운 필드 값을 만들어 제공해야 하는 경우
- 유효성 검사에서 제외됨

`read_only_fields`

- 기존 외래 키 필드 값을 그대로 응답 데이터에 제공하기 위해 지정하는 경우

`read_only` 

- 기존 외래 키 필드 값의 결과를 다른 값으로 덮어쓰는 경우
- 새로운 응답 데이터 값을 제공하는 경우

### API 문서화

OpenAPI Specification(OAS)

- RESTful API를 설명하고 시각화하는 표준화된 방법
- API에 대한 세부사항을 기술할 수 있는 공식 표준

[OAS 기반 API에 대한 문서를 생성하는 데 도움을 주는 오픈소스 프레임워크]

https://swagger.io/

https://github.com/Redocly/redoc

### 문서화 활용

`drf-spectacular` 라이브러리 : DRF 위한 OpenAPI 3.0 구조 생성을 도와주는 라이브러리

- 설치
    
    ```python
    $ pip install drf-spectacular
    ```
    
- 등록
    
    ```python
    # settings.py
    
    INSTALLED_APPS = [
    		...,
        'drf_spectacular',
        ...,
    ]
    ```
    
- 관련 설정 코드 입력(OpenAPI 구조 자동 생성 코드)
    
    ```python
    # settings.py
    
    REST_FRAMEWORK = {
        # YOUR SETTINGS
        'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    }
    ```
    
- swagger, redoc 페이지 제공을 위한 url 작성
    
    ```python
    drf/urls.py
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
    
    urlpatterns = [
    		...,
        # YOUR PATTERNS
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        # Optional UI:
        path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
    ```
    

“설계 우선” 접근법

- OAS의 핵심 이점
- API를 먼저 설계하고 명세를 작성한 후, 이를 기반으로 코드를 구현하는 방식
- API의 일관성을 유지하고, API 사용자는 더 쉽게 API를 이해하고 사용할 수 있음
- 또한, OAS를 사용하면 API가 어떻게 작동하는지를 시각적으로 보여주는 문서를 생성할 수 있으며, 이는 API를 이해하고 테스트하는 데 매우 유용
- 이런 목적으로 사용되는 도구가 `Swagger-UI` 또는 `ReDoc`

---

### 참고

### 올바르게 404 응답하기

클라이언트에게 원인이 정확하지 않은 에러를 제공하기 보다는,
적절한 예외 처리를 통해 클라이언트에게 보다 정확한 에러 현황을 전달하기 위함

Django shortcuts functions :

- `render()`
- `redirect()`
- `get_object_or_404()`
    
    모델 manager objects에서 `get()`을 호출하지만, 
    해당 객체가 없을 땐 기존 `DoesNotExist` 예외 대신 `Http404`를 `raise`함
    
    ```python
    # articles/views.py
    
    from django.shortcuts import get_object_or_404
    
    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)
    
    # 위코드를 모두 다음과 같이 변경
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    ```
    
- `get_list_or_404()`
    
    모델 manager objects에서 `filter()`의 결과를 반환하고, 
    해당 객체 목록이 없을 땐 `Http404`를 `raise`함
    
    ```python
    # articles/views.py
    
    from django.shortcuts import get_object_or_404, get_list_or_404
    
    article = Article.objects.all()
    comment = Comment.objects.all()
    
    # 위코드를 모두 다음과 같이 변경
    article = get_list_or_404(Article)
    comment = get_list_or_404(Comment)
    ```
    

### 복잡한 ORM 활용

[ORM 활용 시 권장 방식]

복잡한 query나 로직은 view 함수에서 진행

- 여러 모델을 조인하거나 복잡한 집계가 필요한 경우 view 함수에서 처리
- 필요한 경우 view 함수에서 `select_related()`나 `prefetch_related()`를 사용하여 query를 최적화

serializer는 기본적인 데이터 변환을 담당

- serializer만으로는 복잡한 query를 처리하기 어려움