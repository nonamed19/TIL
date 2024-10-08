### 2차원 배열 :

`arr = [[0, 1, 2, 3],[4, 5, 6, 7]]`

1차원 list를 묶어놓은 list

2차원 이상의 다차원 list는 차원에 따라 Index를 선언

2차원 list의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함

Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

```python
N = int(input)
arr = [list(map(int, input().split())) for _  in range(N)]
arr = [list(map(int, input())) for _ in range(N)]
```

<br>

### 배열 순회 :

n x m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법

행 우선 순회

```
# i 행의 좌표
# j 열의 좌표
for i in range(n):
    for j in range(m):
        f(array[i][j]) # 필요한 연산 수행
```

열 우선 순회

```
# i 행의 좌표
# j 열의 좌표
for j in range(m):
    for i in range(n):
        f(array[i][j]) # 필요한 연산 수행
```

지그재그 순회

```
# i 행의 좌표
# j 열의 좌표
for i in range(n):
    for j in range(m):
        f(array[i][j + (m-1-2*j)*(i%2)]) # 필요한 연산 수행
```

- `i%2` 는 현재 행이 짝수인지 홀수인지 판별합니다.
- 짝수 행 (`i%2 == 0`): `j + (m-1-2*j)*(0)` => `j`
- 홀수 행 (`i%2 == 1`): `j + (m-1-2*j)*(1)` => `j + (m-1-2*j)` => `m-1-j`

<br>

### 델타를 이용한 2차 배열 탐색 :

2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

인덱스 `(i, j)`인 칸의 상하좌우 칸 `(ni, nj)`

![Untitled](./Pictures/Untitled.png)

```python
arr[0...N-1][0...N-1] # NxN 배열
di[] <- [0, 1, 0, -1]
dj[] <- [1, 0, -1, 0]
for i: 0 -> N-1
    for j: 0 -> N-1
        for k in range(4):
            ni <- i + di[k]
            nj <- j + dj[k]
            if 0 <= ni <= N and 0 <= nj < N # 유효한 인덱스면
                f(arr[ni][nj])
```

### 전치 행렬 :

```python
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1,2,3],[4,5,6],[7,8,9]] # 3*3 행렬

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

![Untitled](./Pictures/Untitled%20(1).png)

<br>

### 부분집합 합(Subset Sum) 문제 :

유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지를 알아내는 문제

예를 들어, [-7, -3, -2, 5, 8]라는 집합이 있을 때, [-3, -2, 5]는 이 집합의 부분집합이면서 (-3)+(-2)+5=0이므로 이 경우의 답은 참이 된다.

완전검색 기법으로 부분집합 합 문제를 풀기 위해서는, 우선 집합의 모든 부분집합을 생성한 후에 각 부분집합의 합을 계산해야 한다.

부분집합의 수

집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 개수는 2^n개이다.

이는 각 원소를 부분집합에 포함시키거나 포함시키지 않는 2가지 경우를 모든 원소에 적용한 경우의 수와 같다.

ex. {1, 2, 3, 4} → 2 x 2 x 2 x 2 = 16가지

```python
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i                # 0번 원소
    for j in range(2):
        bit[1] = j            # 1번 원소
        for k in range(2):
            bit[2] = k        # 2번 원소
            for l in range(2):
                bit[3] = l    # 3번 원소
                print_subset(bit)
```

비트 연산자

`&` : 비트 단위로 AND 연산을 한다.

`>` : 비트 단위로 OR 연산을 한다. 

`<<` : 피연산자의 비트 열을 왼쪽으로 이동시킨다.

`>>` : 피연산자의 비트 열을 오른쪽으로 이동시킨다.

`<<` 연산자 :

`1 << n : 2^n` 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.

`&` 연산자 :

`i & (i<<j)` : i의 j번째 비트가 1인지 아닌지를 검사한다.

### 보다 간결하게 부분집합을 생성하는 방법 :

```python
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)    # n: 원소의 개수

for i in range(1<<n):    # 1<<n: 부분 집합의 개수
    for j in range(n):   # 원소의 수만큼 비트를 비교함
        if i & (1<<j):   # i의 j번 비트가 1인 경우
            print(arr[j], end=",")    # j번 원소 출력
    print()
print()
```

<br>

### 검색(Search) :

저장되어 있는 자료 중에서 원하는 항목을 찾는 작업

목적하는 탐색 키를 가진 항목을 찾는 것

- 탐색 키(search key) : 자료를 구별하여 인식할 수 있는 키

### 검색의 종류 :

- 순차 검색(sequential search) : 일렬로 되어 있는 자료를 순서대로 검색하는 방법
    
    가장 간단하고 직관적인 검색 방법
    
    배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
    
    알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임
    
    - 정렬되어 있지 않은 경우
        1. 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.
        2. 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
        3. 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패
        
        정렬되지 않은 자료에서의 순차 검색의 평균 비교 회수
        
        $$
        (1/n)*(1+2+3+…+n) = (n+1)/2
        $$
        
        시간 복잡도 : O(n)
        
        ```python
        def sequential_search(a, n, key)
            i <- 0
            while i < n and a[i] != key:
                i <- i + 1
            if i < n: return i
            else: return -1
        ```
        
    - 정렬되어 있는 경우
        
        자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료한다.
        
        정렬이 되어 있으므로, 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줄어든다.
        
        시간 복잡도 : O(n)
        
        ```python
        def sequentialSearch2(a, n, key)
            i <- 0
            while i < n and a[i] < key: # index 확인은 value의 비교보다 먼저 수행되어야 함
                i <- i + 1
            if i < n and a[i] == key: return i
            else: return -1
        ```
        
- 이진 검색(binary search) : 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
    
    목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행
    
    이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다
    
    검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행한다
    
    이진 검색을 수행할 때, 자료에 삽입이나 삭제가 발생하는 경우 배열의 상태를 항상 정렬 상태로 유지하는 추가 작업이 필요하다.
    
    ```python
    def binarySearch(a, N, key)
        start = 0
        end = N - 1
        while start <= end:
            middle = (start + end)//2
            if a[middle] == key: # 검색 성공
                return true
            elif a[middle] > key:
                end = middle - 1
            else:
                start = middle + 1
        return fasle # 검색 실패
    ```
    
    재귀 함수 이용
    
    ```python
    def binarySearch2(a, low, high, key):
        if low > high: # 검색 실패
            return False
        else:
            middle = (low + high)//2
            if key == a[middle]: # 검색 성공
                return True
            elif key < a[middle]:
                return binarySearch2(a, low, middle-1, key)
            elif a[middle] < key:
                return binarySearch2(a, middle+1, high, key)
    ```
    
- 해쉬(hash)
    
<br>

### 인덱스 (or Look up table) : 테이블에 대한 동작 속도를 높여주는 자료 구조

인덱스라는 용어는 Database에서 유래함

인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 디스크 공간보다 작다. (인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지 않기 때문)

대량 데이터의 성능 저하 문제를 해결하기 위해 배열 인덱스를 사용함

데이터베이스의 인덱스는 이진 탐색 트리 구조로 되어있음

<br>

### 선택 정렬(Selection Sort) :

주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

- 앞서 살펴본 Selection 알고리즘을 전체 자료에 적용한 것
1. 주어진 리스트 중에서 최소값을 찾는다.
2. 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.

시간 복잡도 : O(n^2)

- 선택 정렬 알고리즘 in pseudo code
    
    ```python
    def SelectionSort(a[], n)
        for i from 0 to n-2
            a[i], ..., a[n-1] 원소 중 최소값 a[k] 찾음
            a[i]와 a[k] 교환
    ```
    
- 선택 정렬 알고리즘 in python code
    
    ```python
    def selectionSort(a, N):
        for i in range(N-1):
            min_idx = i
            for j in range(i+1, N):
                if a[min_idx] > a[j]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
    ```
    
- 선택 정렬 알고리즘 example in python code
    
    ```python
    def selection_sort(arr, N): # arr 정렬대상, N 크기
        for i in range(N-1):     # 주어진 구간에 대해 ... 기준 위치 i를 정하고
            min_idx = i         # 최솟값 위치를 기준위치로 가정
            for j in range(i+1, N):   # 남은 원소에 대해 실제 최솟값 위치 검색
              if arr[min_idx] > arr[j]:
                min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    A = [2, 7, 5, 3, 4]
    B = [4, 3, 2, 1]
    
    selection_sort(A, len(A))
    selection_sort(B, len(B))
    ```
    
<br>

### 셀렉션 알고리즘(Selection Algorithm) :

저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘이라 한다.

- 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다.

셀렉션은 아래와 같은 과정을 통해 이루어진다.

- 정렬 알고리즘을 이용하여 자료 정렬하기
- 원하는 순서에 있는 원소 가져오기

시간 복잡도 : O(kn)

- k번째로 작은 원소를 찾는 알고리즘 in python code
    
    ```python
    def select(arr, k):
        for i in range(0, k):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr[k-1]
    ```