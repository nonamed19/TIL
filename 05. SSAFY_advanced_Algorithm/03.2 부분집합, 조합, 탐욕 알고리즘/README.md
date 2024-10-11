### 부분 집합 :

집합에 포함된 원소들을 선택하는 것

부분집합에는 아무것도 선택하지 않은 경우도 집합에 포함됨(= 공집합)

완전 탐색 : 재귀호출을 이용한 완전탐색으로 부분집합을 구할 수 있음(비추천)

- *중복을 허용하지 않는 순열을 통해 index를 구하는 방식*

```python
def run(lev):
    if lev == 3:
        lst_idx.append(path[:])
        return

    for i in range(2):
        path.append(arr[i])
        run(lev + 1)
        path.pop()

arr = ['O', 'X']
lst = ['MIN', 'CO', 'TIM']
path = []
lst_idx = []

run(0)

result = []
for idx in lst_idx:
    temp = []
    for i in range(len(idx)):
        if idx[i] == 'O':
            temp.append(lst[i])
    result.append(temp)

print(result)
```

Binary Counting : 2진수 & 비트연산을 이용하여, 부분집합을 구할 수 있음(추천)

- *원소 수에 해당하는 N개의 비트열을 이용*

```python
def get_sub(tar):
    for i in range(n):
        if tar & 0x1: # 1, 0b1, 0o1, 0x1으로 써도 무관함. 비트 연산임을 나타내기 위한 관례.
            print(arr[i], end = ' ')
        tar >>= 1

arr = ['A', 'B', 'C']
n = len(arr)

for tar in range(0, 1 << n): # range(0, 8)
    print('{', end = ' ')
    get_sub(tar)
    print('}')
```

```python
def get_sub(tar):
    cnt = 0 # 1의 개수를 cnt
    for i in range(n):
        if tar & 0x1: # 1, 0b1, 0o1, 0x1으로 써도 무관함. 비트 연산임을 나타내기 위한 관례.
            # print(arr[i], end = ' ')
            cnt += 1
        tar >>= 1
    return cnt

arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

result = 0
for tar in range(0, 1 << n):
    if get_sub(tar) >= 2:
        result += 1

print(result)
```

### 조합(Combination) :

서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것

ex. 5명 중 n명을 뽑는 코드를 구현하기 위해서는

→ n중 for문(Branch : 5개, Level : n)으로 구현이 가능함. 즉, 재귀호출 구현이 필요

```python
arr = ['A', 'B', 'C', 'D', 'E']
path = []
n = 3

def run(lev, start):
    if lev == n:
        print(*path)
        return

    for i in range(start, 5):
        path.append(arr[i])
        run(lev + 1, i + 1)
        path.pop()

run(0, 0)
```

### Greedy(욕심장이기법, 알고리즘) :

결정이 필요할 때, 현재 기준으로 가장 좋아 보이는 선택지로 결정하여 답을 도출하는 알고리즘

대표적인 문제 해결 기법 :

- 완전 탐색(Brute-Force)
    
    답이 될 수 있는 모든 경우를 시도해보는 알고리즘
    
- Greedy
    
    결정이 필요할 때 가장 좋아보이는 선택지로 결정하는 알고리즘
    
- DP
    
    현재에서 가장 좋아 보이는 것을 선택하는 것이 아니라, 과거의 데이터를 이용하여, 현재의 데이터를 만들어내는 문제해결기법
    
- 분할정복
    
    큰 문제를 작은 문제로 나누어 해결하는 문제해결기법
    

ex. 0-1 Knapsack 문제

- 해당 문제는 kg당 가치가 가장 높은 것을 담으면 될 것 같이 보이지만,
- 해당 문제는 그리디로 해결할 수 없는 문제로 완전탐색 or DP로 접근해야 함

ex. Factional Knapsack 문제

- 0-1 Knapsack과 달리, 물건을 원하는 만큼 자를 수 있는 Knapsack 문제.
- 해당 문제는 그리디가 성립하는 문제로, kg당 가치가 가장 높은 것을 최대한 담으면 됨

ex. 활동 선택(Activity-selection) 문제

1. 끝나는 시간을 기준으로 오름차순 정렬한다
2. 빠르게 끝나는 회의를 선택하여 확정한다
3. 이후로 가능한 회의 중, 빠르게 끝나는 회의를 선택하여 확정한다