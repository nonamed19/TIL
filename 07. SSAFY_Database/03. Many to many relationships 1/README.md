### Many to many relationships (N:M or M:N)

한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우

→ 양쪽 모두에서 N:1 관계를 가짐

### N:1의 한계

case) 의사와 환자 간 모델 관계

`hospital_doctor`

| id | name |
| --- | --- |
| 1 | allie |
| 2 | barbie |

`hospitals_patient`

| id | name | doctor_id |
| --- | --- | --- |
| 1 | carol | 1 |
| 2 | duke | 2 |
| 3 | carol | 2 |
| 4 | carol | 1, 2 |
- 1번 환자가 두 의사 모두에게 진료를 받고자 한다면 환자 테이블에 1번 환자 데이터가 중복으로 입력될 수 밖에 없음
- 동일한 환자지만 다른 의사에게도 진료 받기 위해 예약하기 위해서는 객체를 하나 더 만들어 진행해야 함
- 외래 키 컬럼에 `‘1, 2’` 형태로 저장하는 것은 DB 타입 문제로 불가능
- “`ForeignKey`”를 저장하는 table을 따로 생성하자 !!

### 중개 모델

- 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 생성
- 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐(through `ForeignKey`)

`hospital_doctor`

| id | name |
| --- | --- |
| 1 | allie |
| 2 | barbie |

`hospitals_patient`

| id | name |
| --- | --- |
| 1 | carol |
| 2 | duke |

`hospitals_reservation`

| id | doctor_id | patient_id |
| --- | --- | --- |
| 1 | 1 | 1 |
| 2 | 1 | 2 |
- Django에서는 `‘ManyToManyField’`로 중개모델을 자동으로 생성

### ManyToManyField

`ManyToManyField()` : M:N 관계 설정 모델 필드

- M:N 관계로 맺어진 두 테이블에는 물리적인 변화가 없음
- 환자(or 의사) 모델에 `ManyToManyField` 작성 - 참조/역참조 관계에 유의

```python
class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

- 예약 생성(환자가 예약)

```python
In [4]: patient1.doctors.add(doctor1)

In [5]: patient1.doctors.all()
Out[5]: <QuerySet [<Doctor: 1번 의사 allie>]>

In [6]: doctor1.patient_set.all()
Out[6]: <QuerySet [<Patient: 1번 환자 carol>]>
```

- 예약 생성(의사가 예약)

```python
In [7]: doctor1.patient_set.add(patient2)

In [8]: doctor1.patient_set.all()
Out[8]: <QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 duke>]>
```

- 예약 현황 확인

```python
In [9]: patient1.doctors.all()
Out[9]: <QuerySet [<Doctor: 1번 의사 allie>]>

In [10]: patient2.doctors.all()
Out[10]: <QuerySet [<Doctor: 1번 의사 allie>]>
```

| id | patient_id | doctor_id |
| --- | --- | --- |
| 1 | 1 | 1 |
| 2 | 2 | 1 |
- 예약 취소하기(삭제) - `.remove()`

```python
# doctor1이 patient1 진료 예약 취소

In [11]: doctor1.patient_set.remove(patient1)

In [12]: doctor1.patient_set.all()
Out[12]: <QuerySet [<Patient: 2번 환자 duke>]>

In [13]: patient1.doctors.all()
Out[13]: <QuerySet []>
```

```python
# patient2가 doctor1 진료 예약 취소

In [15]: patient2.doctors.remove(doctor1)

In [16]: patient2.doctors.all()
Out[16]: <QuerySet []>

In [17]: doctor1.patient_set.all()
Out[17]: <QuerySet []>
```

### `‘through’` argument

중개 테이블에 ‘추가 데이터’를 사용해 M:N 관계를 형성하려는 경우에 사용

- 예약 생성 방법 1 : Reservation class를 통한 예약 생성
- 예약 생성 방법 2 : Patient 또는 Doctor의 인스턴스를 통한 예약 생성(`through_defaults`)

```python
In [12]: patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})

In [13]: doctor1.patient_set.all()
Out[13]: <QuerySet [<Patient: 2번 환자 duke>]>

In [14]: patient2.doctors.all()
Out[14]: <QuerySet [<Doctor: 1번 의사 allie>]>
```

### ManyToManyField

`ManyToManyField(to, **options)` : M:N 관계 설정 시 사용하는 모델 필드

- 양방향 관계 : 어느 모델에서든 관련 객체에 접근할 수 있음
- 중복 방지 : 동일한 관계는 한 번만 저장됨

[ManyToManyField의 대표 인자]

- `‘related_name’` arguments
    
    역참조시 사용하는 manager name을 변경
    
    ```python
    class Patient(models.Model):
        doctors = models.ManyToManyField(Doctor, related_name='patients')
        name = models.TextField()
    ```
    
    ```python
    # 변경 전
    doctor.patient_set.all()
    
    # 변경 후 (변경 후 이전 manager name은 사용 불가)
    doctor.patients.all()
    ```
    
- `‘symmetrical’` arguments
    
    관계 설정 시 대칭 유무 설정, 기본 값 : `True`
    
    `ManyToManyField`가 동일한 모델을 가리키는 정의에서만 사용
    
    ```python
    class Person(models.Model):
        friends = models.ManyToManyField('self')
        # friends = models.ManyToManyField('self', symmetrical=False)
    ```
    
    True일 경우 :
    
    source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)
    
    False일 경우 :
    
    `True`와 반대
    
- `‘through’` arguments
    
    사용하고자 하는 중개모델을 지정
    
    일반적으로 “추가 데이터를 M:N 관계와 연결하려는 경우’에 활용
    
    ```python
    class Patient(models.Model):
        doctors = models.ManyToManyField(Doctor, through='Reservation')
    ```
    

[M:N에서의 대표 조작 methods]

- `add()`
    
    관계 추가
    
    “지정된 객체를 관련 객체 집합에 추가”
    
- `remove()`
    
    관계 제거
    
    “관련 객체 집합에서 지정된 모델 객체를 제거”
    

### 좋아요 기능 구현

- 모델 관계 설정
    
    Article 클래스에 ManyToManyField 작성
    
    `like_users` 필드 생성 시 자동으로 역참조 매니저 `.article_set`가 생성됨
    
    그러나, 이전 N:1 관계에서 이미 같은 이름의 매니저를 사용 중임에 따라 에러가 발생함
    
    따라서, user와 관계된 `ForeignKey` 혹은 `ManyToManyField` 둘 중 하나에 `related_name` 작성 필요 
    
    ```python
    class Article(models.Model):
        user = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
        like_users = models.ManyToManyField(
            settings.AUTH_USER_MODEL, related_name='like_articles'
            )
        title = models.CharField(max_length=10)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    ```
    
- url 작성
    
    ```python
    # articles/urls.py
    
    urlpatterns = [
        ...
        path('<int:article_pk>/likes/', views.likes, name='likes'),
    ]
    ```
    
- view 함수 작성
    
    ```python
    # article/views.py
    
    @login_required
    def likes(request, article_pk):
        # 어떤 글에 좋아요를 눌렀는지 글을 먼저 조회
        article = Article.objects.get(pk=article_pk)
    
        # 좋아요를 추가하는 것이냐 / 취소하는 것이냐
        # 만약 좋아요를 요청한 유저가 해당 글의 좋아요를 누른 유저 목록에 포함되어 있다면 (좋아요 취소)
        if request.user in article.like_users.all():
            article.like_users.remove(request.user)
        # 그게 아니라 좋아요를 요청한 유저가 해당 글의 좋아요를 누른 유저 목록에 없다면 (좋아요 추가)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    ```
    
- index 템플릿에 좋아요 버튼 출력
    
    ```python
    {% for article in articles %}
    	...
      <form action="{% url "articles:likes" article.pk%}" method="POST">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <input type="submit" value="좋아요 취소">
        {% else %}
          <input type="submit" value="좋아요">
        {% endif %}
      </form>
      <hr>
    {% endfor %}
    ```