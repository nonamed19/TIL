[개요]

과학자, 수학자가 모든 이론을 새로 만들거나 증명하지 않는 것처럼 개발자 또한 프로그램 전체를 모두 혼자 힘으로 작성하는 것은 드문 일

다른 프로그래머가 이미 작성해 놓은 수천, 수백만 줄의 코드를 활용하는 것은 생산성에서 매우 중요한 일

### 모듈(Module) :

한 파일로 묶인 변수와 함수의 모음.
특정한 기능을 하는 코드가 작성된 파이썬 파일 (.py)

ex. `math` 내장 모듈 : 파이썬이 미리 작성해 둔 수학 관련 변수와 함수가 작성된 모듈

모듈을 가져오는 방법

- **⭐**`import`문 사용 ← 해당 방법이 더 명시적임
    
    ```python
    import math
    
    print(math.sqrt(4))
    ```
    
- `from`절 사용
    
    ```python
    from math import sqrt
    
    print(sqrt(4))
    ```
    

모듈 사용하기

‘ `. (dot)` ‘ 연산자

“점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라”라는 의미

- 모듈 주의사항
서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
마지막에 import된 이름으로 대체됨
    
    ```python
    from math import pi, sqrt
    from my_math import sqrt
    
    # 그래서 모듈 내 모든 요소를 한번에 import하는 * 표기는 권장하지 않음
    from math import *
    ```
    

‘ `as` ‘ 키워드

`as` 키워드를 사용하여 별칭(alias)을 부여

- 두 개 이상의 모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올 때 발생하는 이름 충돌 해결
    
    ```python
    from math import pi, sqrt
    from my_math import sqrt as my_sqrt
    
    sqrt(4)
    my_sqrt(4)
    ```
    

### 파이썬 표준 라이브러리(Python Standard Library, PSL)

파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

### 패키지(Package)

연관된 모듈들을 하나의 디렉토리에 모아 놓은 것

- PSL 내부 패키지 : 설치 없이 바로 `import`하여 사용
- 외부 패키지 : pip를 사용하여 설치 후 `import` 필요

pip : 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템

https://pypi.org/

패키지 사용 목적 : 

모듈들의 이름공간을 구분하여 충돌을 방지.
모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할

- 패키지 설치
    
    ```python
    $ pip install SomePackage         # 최신 버전
    $ pip install SomePackage==1.0.5  # 특정 버전
    $ pip install SomePackage>=1.0.4  # 최소 버전
    ```
    
- `requests` 외부 패키지 설치 및 사용 예시
    
    https://requests.readthedocs.io/en/latest/#
    
    ```python
    $ pip install requests
    ```
    
    ```python
    import requests
    
    url = 'https://random-data-api.com/api/2/users'
    response = requests.get(url).json()
    
    print(response)
    ```
    
    api를 받은 후 자료를 parsing하기 위해서 크롬 확장 프로그램이 필요함 
    
    https://chromewebstore.google.com/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=ko&pli=1
    

### 제어문(Control Statement) :

코드의 실행 흐름을 제어하는 데 사용되는 구문.
조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행

- 조건문 : `if`, `elif`, `else`
- 반복문 : `for`, `while`
- 반복문 제어 : `break`, `continue`, `pass`

### 조건문(Conditional Statement) :

주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

`if` statement의 기본 구조 :

```python
if 표현식 :
    코드 블록
elif 표현식 :
    코드 블록
else :
    코드 블록
```

복수 조건문 : 조건식을 동시에 검사하는 것이 아니라 “순차적”으로 비교

### 반복문(Loop Statement) :

주어진 코드 블록을 여러번 반복해서 실행하는 구문

`for` : 특정 작업을 반복적으로 수행

`while` : 주어진 조건이 참인 동안 반복해서 실행

### `for`문 :

임의의 시컨스의 항목들을 그 시퀀스에 들어있는 순서대로 반복

- 반복 횟수가 명확하게 정해져 있는 경우에 유용
- 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때

`for statement`의 기본 구조

```python
for 변수 in 반복 가능한 객체 :
    코드 블록
```

- 반복 가능한 객체(iterable) :
반복문에서 순회할 수 있는 객체
(시퀀스 객체 뿐만 아니라 `dict`, `set` 등도 포함)
    
    ```python
    items = ['apple', 'banana', 'coconut']
    
    for item in items :
        print(item)
    ```
    
    ```python
    apple
    banana
    coconut
    ```
    
- 문자열 순회
    
    ```python
    country = 'Korea'
    
    for char in country :
        print(char)
    ```
    
    ```python
    
    K
    o
    r
    e
    a
    ```
    
- range 순회
    
    ```python
    for i in range(5) :
        print(i)
    ```
    
    ```python
    0
    1
    2
    3
    4
    ```
    
- 딕셔너리 순회
    
    ```python
    my_dict = {
        'x' : 10,
        'y' : 20,
        'z' : 30,
    }
    
    for key in my_dict :
        print(key)
        print(my_dict[key])
    ```
    
    ```python
    x
    10
    y
    20
    z
    30
    ```
    
- 인덱스로 리스트 순회
리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경하기
    
    ```python
    numbers = [4, 6, 10, -8, 5]
    
    for i in range(len(numbers)) :
        numbers[i] = numbers[i] * 2
    
    print(numbers)
    ```
    
    ```python
    [8, 12, 20, -16, 10]
    ```
    
- 중첩된 반복문
    
    ```python
    outers = ['A', 'B']
    inners = ['c', 'd']
    
    for outer in outers :
        for inner in inners :
            print(outer, inner)
    ```
    
    ```python
    A c
    A d
    B c
    B d
    ```
    

### `while` 문 :

주어진 조건식이 참(True)인 동안 코드를 반복해서 실행
== 조건식이 거짓(False)가 될 때까지 반복

- 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
- 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

**⭐**`while`문은 반드시 종료 조건이 필요**⭐**

`while statement`의 기본 구조

```python
while 조건식 :
    코드 블록
```

### 반복 제어 :

`for`문과 `while`문은 매 반복마다 본문 내 모든 코드를 실행하지만 때때로 일부만 실행하는 것이 필요할 때가 있음

- break : 반복을 즉시 중지
    
    ```python
    for i in range(10) :
        if i == 5 :
            break
        print(i)
    ```
    
- continue : 다음 반복으로 건너뜀
    
    ```python
    for i in range(10) :
        if i % 2 == 0 :
            continue
        print(i)
    ```
    
- pass : 아무런 동작도 수행하지 않고 넘어감
    
    ```python
    for i in range(10) :
        pass
    ```
    

flag variable : signal in programming to let the program know that a certain condition has met

### List Comprehension :

간결하고 효율적인 리스트 생성 방법

`list comprehension`의 기본 구조

```python
[expression for 변수 in iterable]

[expression for 변수 in iterable if 조건식]
```

- list comprehension 사용 전 :
    
    ```python
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = []
    
    for num in numbers:
        squared_numbers.append(num**2)
    
    print(squared_numbers)
    ```
    
- list comprehension 사용 후 :
    
    ```python
    numbers = [1, 2, 3, 4, 5]
    
    squared_numbers2 = [num**2 for num in numbers]
    
    print(squared_numbers)
    ```
    
    ```python
    numbers = [1, 2, 3, 4, 5]
    squared_numbers2 = list(num**2 for num in numbers)
    
    print(squared_numbers)
    ```
    

활용 예시1 - 2차원 배열 생성 시 (인접행렬 생성 시)

```python
data1 = [[0] * (5) for _ in range(5)]

# 또는
data2 = [[0 for _ in range(10)] for _ in range(10)]
```

```python
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]
```

활용 예시2

```python
result = [i for i in range(10) if i % 2 == 1]
```

```python
result = []
for i in range(10) :
    if i % 2 == 1 :
        result.append(i)
```

### 모듈 내부 살펴보기

내장 함수 `help`를 사용해 모듈에 무엇이 들어있는지 확인 가능

### enumerate 함수

iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

`enumerate(iterable, start = 0)`

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits, 0) :
    print(f'인덱스 {index} : {fruit}')
```

```python
인덱스 0 : apple
인덱스 1 : banana
인덱스 2 : cherry
```