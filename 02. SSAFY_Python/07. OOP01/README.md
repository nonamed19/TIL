### 절차 지향 프로그래밍(Procedural Programming) :

프로그램을 ‘데이터’와 ‘절차’로 구성하는 방식의 프로그래밍 패러다임

‘데이터’와 해당 데이터를 처리하는 ‘함수(절차)’가 분리되어 있으며, 함수 호출의 흐름이 중요

코드의 순차적인 흐름과 함수 호출에 의해 프로그래밍이 진행

- 실제로 실행되는 내용이 무엇이 무엇인가가 중요
- 데이터를 다시 재사용하거나 하기보다는 처음부터 끝까지 실행되는 결과물이 중요한 방식

소프트웨어 위기(Software Crisis) :

하드웨어의 발전으로 컴퓨터 계산용량과 문제의 복잡성이 급격히 증가함에 따라 소프트웨어에 발생한 충격

<br></br>

### 객체 지향 프로그래밍(Object Oriented Programming) :

데이터와 해당 데이터를 조작하는 메서드를 하나의 객체로 묶어 관리하는 방식의 프로그래밍 패러다임

| 절차 지향 | 객체 지향 |
| --- | --- |
| 데이터와 해당 데이터를 처리하는 함수(절차)가 분리 | 데이터와 해당 데이터를 처리하는 메서드(메시지)를 하나의 객체(클래스)로 묶음 |
| 함수 호출의 흐름이 중요 | 객체 간 상호작용과 메세지 전달이 중요 |
<br></br>

**⭐절차 지향과 객체 지향은 대조되는 개념이 아니다⭐**

객체 지향은 기존 절차 지향을 기반으로 두고 보완하기 위해 객체라는 개념을 도입해 상속, 코드 재사용성, 유지보수성 등의 이점을 가지는 패러다임

<br></br>

### 클래스(Class) :

파이썬에서 타입을 표현하는 방법

- 객체를 생성하기 위한 설계도
- 데이터와 기능을 함께 묶는 방법을 제공

클래스 이름은 파스칼 케이스(Pascal Case) 방식으로 지정

*카멜 케이스(Camel Case) : 문자열의 첫 문자를 제외하고 단어의 첫 글자마다 대문자로 표현 for conventional*

*케밥 케이스(Kebab Case) : 모두 소문자로 표현하며 단어와 단어 사이를 대시(-)로 표현 for yml file or url*

*스네이크 케이스(Snake Case) : 소/대문자로 표현하며 단어와 단어 사이를 언더스코어(_)로 표현 for constants*

*파스칼 케이스(Pascal Case) : 문자열 내 모든 단어의 첫 글자마다 대문자로 표현 for Class(Python)*

### 객체(Object) :

클래스에서 정의한 것을 토대로 메모리에 할당된 것
’속성’과 ‘행동(기능)’으로 구성된 모든 것

- 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가 ?
- 속성(attribute) : 어떤 상태(데이터)를 가지는가 ?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가 ?

### 인스턴스(Instance) :

클래스의 속성과 행동을 기반으로 생성된 개별 객체

→ 하나의 객체(object)는 특정 타입의 인스턴스(instance)이다.

ex. 123, 900, 5는 모두 int의 인스턴스

ex. ‘hello’, ‘bye’는 모두 string의 인스턴스

ex. [232, 89, 1], [ ]은 모두 list의 인스턴스

<br></br>

### 클래스 구성요소 :

```python
# 클래스 정의
class Person:
    blood_color = 'red'

    def __init__(self, name):
        self.name = name
    
    def singing(self) :
        return f'{self.name}가 노래합니다.'

# 인스턴스 생성
singer1 = Person('iu')

# (인스턴스) 메서드 호출
print(singer1.singing())

# 속성(변수) 접근
print(singer1.blood_color)

# 인스턴스 속성(변수)
print(singer1.name)
```

- 생성자 메서드 :
    
    객체를 생성할 때 자동으로 호출되는 특별한 메서드
    
    `__init__` 이라는 이름의 메서드로 정의되며, 객체의 초기화를 담당
    
    생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정
    
    → 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정 가능
    
    ```python
    def __init__(self, name):
            self.name = name
            Person.count += 1
    ```
    
- 인스턴스 변수 :
    
    인스턴스(객체)마다 별도로 유지되는 변수
    
    인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화됨
    
- 클래스 변수 :
    
    클래스 내부에 선언된 변수
    
    클래스로 생성된 모든 인스턴스들이 공유하는 변수
    
- 인스턴스 메서드 :
    
    각각의 인스턴스에서 호출할 수 있는 메서드
    
    인스턴스 변수에 접근하고 수정하는 등의 작업을 수행
    
<br></br>

### 메서드(Method) :

각자의 메서드는 OOP(Object Oriented Programming) 패러다임에 따라 명확한 목적에 따라 설계된 것이기 때문에 클래스와 인스턴스 각각 올바른 메서드만 사용한다. 

<br></br>

### 인스턴스 메서드(Instance Method) :

클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드

→ 인스턴스의 상태를 조작하거나 동작을 수행

```python
class MyClass:
    def instance_method(self, arg1, ...):
        pass
```

반드시 첫 번째 매개변수로 인스턴스 자신(self)를 전달받음

⭐self는 매개변수 이름일 뿐이며 다른 이름으로 설정 가능하나, 다른 이름을 사용하지 않을 것을 강력히 권장

<br></br>

### 생성자 메서드(Constructor Method) :

인스턴스 객체가 생성될 때 자동으로 호출되는 메서드

→ 인스턴스 변수들의 초기값을 설정

```python
class Person:
    def __init__(self):
        pass
```

```python
class Person:
    def __init__(self, name):
        self.name = name
        print('인스턴스가 생성되었습니다.')
    
    def greeting(self):
        print(f'안녕하세요. {self.name}입니다.')

person1 = Person('지민') # 인스턴스가 생성되었습니다.
person1.greeting() # 안녕하세요. 지민입니다.
```

<br></br>

### 클래스 메서드(Class Method) :

클래스가 호출하는 메서드

→ 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

`@classmethod` 데코레이터를 사용하여 정의

호출 시, 첫번째 인자로 해당 메서__드를 호출하는 클래스`(cls)`가 전달됨

⭐cls는 매개변수 이름일 뿐이며 다른 이름으로 설정 가능하나, 다른 이름을 사용하지 않을 것을 강력히 권장

```python
class MyClass:
    @classmethod
    def class_method(cls, arg1, ...):
        pass
```

```python
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')

person1 = Person('iu')
person2 = Person('BTS')

Person.number_of_population() # 인구수는 2입니다.
```

<br></br>

### 스태틱(정적) 메서드(Static Method) :

클래스, 인스턴스와 상관없이 독립적으로 동작하는 메서드

→ 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용

`@staticmethod` 데코레이터를 사용하여 정의

호출 시 필수적으로 작성해야 할 매개변수가 없음

- 즉, 객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을 위한 메서드로 사용

```python
class MyClass:
    @staticmethod
    def static_method(arg1, ...):
        pass
```

<br></br>

### 인스턴스와 클래스 간 이름 공간

클래스를 정의하면, 클래스와 해당하는 이름 공간 생성

인스턴스를 만들면, 인스턴스 객체가 생성되고 독립적인 이름 공간 생성

인스턴스에서 특정 속성에 접근하면, 인스턴스 → 클래스 순으로 탐색

![Untitled](./Day_8_OOP1/Pictures/Untitled.png)

각 인스턴스는 독립적인 메모리 공간을 가지며, 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능

객체 지향 프로그래밍의 중요한 특성 중 하나로, 클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장

이를 통해 클래스와 인스턴스는 다른 객체들과의 상호작용에서 서로 충돌이나 영향을 주지 않으면서 독립적으로 동작할 수 있음

코드의 가독성, 유지보수성, 재사용성을 높이는 데 도움을 줌

<br></br>

### 매직 메서드(Magic Method) or 스페셜 메서드(Special Method):

특정 상황에 자동으로 호출되는 인스턴스 메서드

Double underscore`(__)`가 있는 메서드는 특수한 동작을 위해 만들어진 메서드

- `__str__(self)`
    
    내장함수 print에 의해 호출되어 객체 출력을 문자열 표현으로 변경
    
<br></br>

### 데코레이터(Decorator)

다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수

```python
# 데코레이터 정의
def my_decorator(func):
    def wrapper():
        # 함수 실행 전에 수행할 작업
        print('함수 실행 전')
        # 원본 함수 호출
        result = func()
        # 함수 실행 후에 수행할 작업
        print('함수 실행 후')
        return result
    return wrapper
```

```python
# 데코레이터 사용
@my_decorator
def my_function():
    print('원본 함수 실행')
my_function()

"""
함수 실행 전
원본 함수 실행
함수 실행 후
"""
```