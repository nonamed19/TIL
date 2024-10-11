커스텀 유저 모델을 사용하려면 다시 작성해야 하는 class Meta: model = User가 작성된 Form :

- UserCreationForm
- UserChangeForm

```python
# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# django는 User 모델을 직접 참조하는 것을 권장하지 않는다.
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)
```

### 회원 가입

User 객체를 Create하는 과정

`UserCreationForm()` :

회원 가입 시 사용자 입력 데이터를 받는 built-in ModelForm

```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]

```

```python
# accounts/views.py

from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
```

```python
# accounts/signup.html

<body>
  <h1>회원가입</h1>
  <form action="{% url "accounts:signup" %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
</body>
```

`get_user_model()` :

현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환하는 함수

Django에서는 User 모델을 직접 참조하는 것 대신 `get_user_model()`을 사용해 커스텀 `User` 모델을 반환 받아 사용하여 참조하는 것을 강조함

### 회원 탈퇴

User 객체를 Delete하는 과정

```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('delete/', views.delete, name='delete'),
]

```

```python
# accounts/views.py

def delete(request):
    request.user.delete()
    return redirect('articles:index')
```

### 회원정보 수정

User 객체를 Update하는 과정

`UserChangeForm()` :

회원정보 수정 시 사용자 입력 데이터를 받는 built-in `ModelForm`

```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('update/', views.update, name='update'),
]
```

```python
# accounts/views.py

from .forms import CustomUserChangeForm

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)
```

### 비밀번호 변경

인증된 사용자의 Session 데이터를 Update 하는 과정

`PasswordChangeForm()` :

비밀번호 변경 시 사용자 입력 데이터를 받는 built-in form

django는 비밀번호 변경 페이지를 회원정보 수정 `form` 하단에서 별도 주소로 안내 :

`/user_pk/password`

```python
# crud/urls.py

from accounts import views

urlpatterns = [
    path('<int:user_pk>/password/', views.change_password, name='change_password'),
]

```

```python
# accounts/views.py

def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)
```

### 세션 무효화 방지

비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어버려 로그인 상태가 유지되지 못하고 로그아웃 처리됨

비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문

`update_session_auth_hash(request, user)` :

암호 변경 시 세션 무효화를 막아주는 함수

→ 암호가 변경되면 새로운 password의 Session data로 기존 session을 자동으로 갱신

```python
# accounts/views.py

from django.contrib.auth import update_session_auth_hash

def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)
```

### 인증된 사용자에 대한 접근 제한

`is_authenticated` 속성 :

사용자가 인증 되었는지 여부를 알 수 있는 User model의 속성

→ 모든 `User` 인스턴스에 대해 항상 `True`인 읽기 전용 속성

→ 비인증 사용자에 대해서는 항상 `False`

- 로그인과 비로그인 상태에서 화면에 출력되는 링크를 다르게 설정하기

```python
# articles/index.html

{% if request.user.is_authenticated %}
  <p>안녕하세요 {{ user.username }}</p>

  <h1>Articles</h1>

  <a href="{% url "articles:create" %}">CREATE</a>
  {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <a href="{% url "articles:detail" article.pk %}">
      <p>글 제목: {{ article.title }}</p>
    </a>
    <p>글 내용: {{ article.content }}</p>
    <hr>
  {% endfor %}

  <form action="{% url "accounts:logout" %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="LOGOUT">
  </form>

  <form action="accounts:delete" method="POST">
    {% csrf_token %}
    <input type="submit" value="회원탈퇴">
  </form>

  <a href="{% url "accounts:update" %}">회원정보 수정</a>

{% else %}
<a href="{% url "accounts:login" %}">LOGIN</a>
<br>
<a href="{% url "accounts:signup" %}">회원가입</a>

{% endif %}
```

- 인증된 사용자라면 로그인/회원가입 로직을 수행할 수 없도록 하기

```python
# accounts/views.py

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
		...

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    ...
```

`login_required` 데코레이터 :

인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터

→ 비인증 사용자의 경우 `/accounts/login/` 주소로 `redirect` 시킴

- 인증된 사용자만 게시글을 작성/수정/삭제 할 수 있도록 수정

```python
# articles/views.py

from django.contrib.auth.decorators import login_required

@login_required
def create(request):
		...

@login_required
def update(request, pk):
		...

@login_required
def delete(request, pk):
		...

```

- 인증된 사용자만 로그아웃/탈퇴/수정/비밀번호 변경 할 수 있도록 수정

```python
# accounts/views.py

from django.contrib.auth.decorators import login_required

@login_required
def logout(request):
		...

@login_required
def delete(request):
		...

@login_required
def update(request):
		...

@login_required
def change_password(request, user_pk):
		...

```

---

### 참고

[`is_authenticated` 속성 코드]

메서드가 아닌 속성 값임을 주의

[회원가입 후 자동 로그인]

회원가입 성공한 user 객체를 활용해 login 진행

```python
# accounts/views.py

def signup(request):
    ...
    if form.is_valid():
        form.save()
        auth_login(request, user)
        ...
```

[회원 탈퇴 개선]

탈퇴와 함께 기존 사용자의 Session Data 삭제 방법

사용자 객체 삭제 이후 로그아웃 함수 호출

% 탈퇴(1) 후 로그아웃(2)의 순서가 바뀌면 안됨 %

```python
# accounts/views.py

def delete(request):
    request.user.delete()
    auth_logout(request)
    ...
```

[`PasswordChangeForm` 인자 순서]

다른 `Form`과 달리 부모 클래스인 SetPasswordForm의 생성자 함수 구성은 user 객체를 첫번째 인자로 받음

[Auth built-in form 코드]

UserCreationForm()

https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L149

UserChangeForm()

https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L170

PasswordChangeForm()

https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L422