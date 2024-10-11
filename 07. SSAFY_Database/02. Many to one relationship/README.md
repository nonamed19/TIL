### 모델 관계

Many to one relationships(N:1 or 1:N) :

한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 단계

![image.png](./Pictures/image.png)

### 댓글 모델 정의

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

`ForeignKey()` : 한 모델이 다른 모델을 참조하는 관계를 설정하는 필드(N:1 관계 표현)

- `ForeignKey` 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형으로 작성하는 것을 권장
- 외래 키는 `ForeignKey` 클래스를 작성하는 위치와 관계없이 테이블의 마지막 필드로 생성됨
- Migration 이후 만들어 지는 필드 이름 : `‘참조 대상 클래스 이름’` + `‘_’` + `‘클래스 이름’`

`ForeignKey(to, on_delete)`

`to` : 참조하는 모델 class 이름

`on_delete` : 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정(데이터 무결성)

`on_delete = models.CASCADE` : 참조 된 객체(부모 객체)가 삭제 될 때 이를 참조하는 모든 객체도 삭제되도록 지정

### 댓글 생성

```python
$ python manage.py shell_plus

...
```

### 역참조

- N:1 관계에서 1에서 N을 참조하거나 조회하는 것 (1 → N)
- 모델 간의 관계에서 관계를 정의한 모델이 아닌, 관계의 대상이 되는 모델에서 연결된 객체들에 접근하는 방식
- N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만, 1은 N에 대한 참조 방법이 존재하지 않아 별도의 역참조 키워드가 필요

`article.comment_set.all()` : 특정 게시글에 작성된 댓글 전체를 조회하는 요청

- article : 모델 인스턴스
- comment_set : related manager(역참조 이름)
- all() : QuerySet API

Related manager

- N:1 혹은 M:N 관계에서 역참조 시에 사용하는 매니저
- `‘objects’` 매니저를 통해 QuerySet API를 사용했던 것처럼 related manager를 통해 QuerySet API를 사용할 수 있게 됨
- N:1 관계에서 생성되는 Related manager의 이름은 `“모델명_set”` 형태로 자동 생성됨
- `comment.article` : 특정 댓글의 게시글 참조(Comment → Article)
- `article.comment_set.all()` : 특정 게시글의 댓글 목록 참조(Article → Comment)

### 댓글 구현

```python
# articles/forms.py

from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
```

- 사용자로부터 댓글 데이터를 입력 받기 위한 `CommentForm` 정의
- `CommentForm`의 출력 필드를 조정하여 외래 키 필드가 출력되지 않도록 함

```python
# articles/views.py

from .forms import ArticleForm, CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

```python
# articles/detail.html

<form action="{% url "articles:delete" article.pk %}" method="POST">
  {% csrf_token %}
  {{ comment_form }}
  <input type="submit" value="삭제">
</form>
```

- detail view 함수에서 `CommentForm`을 사용하여 detail 페이지에 렌더링

```python
# articles/urls.py

urlpatterns = [
		...,
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
```

```python
# articles/detail.html

<form action="{% url "articles:comments_create" article.pk %}" method="POST">
  {% csrf_token %}
  {{ comment_form }}
	<input type="submit">
</form>
```

- url 작성 및 action 값 작성

```python
# articles/views.py

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

- `comments_create` view 함수 정의
- url로 받은 pk 인자를 게시글을 조회하는 데 사용
- `save(commit=False)` : DB에 저장 요청을 보내지 않고 인스턴스만 반환

### 댓글 READ

```python
# articles/views.py

from .forms import ArticleForm, CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

- detail view 함수에서 전체 댓글 데이터를 조회

```python
# articles/detail.html

<h4>댓글 목록</h4>
<ul>
  {% for comment in comments %}
    <li>{{ comment.content }}</li>
  {% endfor %}
</ul>
```

- 전체 댓글 출력 및 확인

### 댓글 DELETE

```python
# articles.urls/py

urlpatterns = [
		...,
    path(
        '<int:pk>/comments/<int:comment_pk>/delete/',
        views.comments_delete,
        name='comments_delete'
    ),
]
```

- 댓글 삭제 url 작성

```python
# articles/views.py

from .models import Article, Comment

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

---

### 데이터 무결성

- 데이터의 신뢰성 확보, 시스템 안정성, 보안 강화
- 데이터베이스에 저장된 데이터의 정확성, 일관성, 유효성을 유지하는 것
- 데이터베이스에 저장된 데이터 값의 정확성을 보장하는 것

### admin site 댓글 등록

`Comment` 모델을 admin site에 등록해 CRUD 동작 확인하기

```python
# articles/admin.py

from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
```

### 댓글 추가 구현

- 댓글이 없는 경우 대체 컨텐츠 출력
    
    DTL의 `‘for empty’` 태그 활용
    
    ```python
    # articles/detail.html
    
    {% for comment in comments %}
      <li>
        {{ comment.content }}
        <form action="{% url "articles:comments_delete" article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
      </li>
    {% empty %}
      <p>댓글이 없어요..</p>
    {% endfor %}
    ```
    
- 댓글 개수 출력하기
    
    DTL filter - ‘length’ 사용
    
    ```python
    {{ comments|length }}
    
    {{ article.comment_set.all|length }}
    ```
    
    QuerySetAPI - `‘count()’` 사용
    
    ```python
    {{ article.comment_set.count }}
    ```