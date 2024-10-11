### 반복(Iteration)과 재귀(Recursion)

반복 : 수행하는 작업이 완료될 때까지 계속 반복

- 루프 (for, while 구조)
- 반복문은 코드를 n번 반복시킬 수 있다.

재귀 : 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법

- 하나의 큰 문제를 해결할 수 있는(해결하기 쉬운) 더 작은 문제로 쪼개고 결과들을 결합한다.
- 재귀호출은 n 중 반복문을 만들어낼 수 있다.

재귀 관련 함수의 특징 :

1. 함수를 호출할 때 int 타입 객체를 전달하면 값만 복사가 됨
2. 함수가 끝나면 Main으로 돌아오는 것이 아니라, 해당 함수를 호출했던 곳으로 돌아옴

재귀호출은 무한 재귀호출을 막는 것이 제일 중요함.

- 기저조건(base case)를 통해 재귀의 종료조건을 설정해야 함.

### 순열(Permutation) :

서로 다른 N개에서, R개를 중복 없이, 순서를 고려하여 나열하는 것

cf) 중복 순열 :

서로 다른 N개에서, R개를 중복을 허용하고, 순서를 고려하여 나열하는 것

중복 순열 구현 원리 :

1. 재귀 호출을 할 때 마다, 이동 경로를 흔적으로 남긴다
2. 가장 마지막 레벨에 도착했을 때, 이동 경로(흔적)를 출력한다
이 때, path에 적은 마지막 기록이 삭제 되어야 한다.

```python
path = []

def KFC(x):
    if x == 2:
        print(path)
        return

    for i in range(3):
        path.append(i)
        KFC(x+1)
        path.pop()

KFC(0)
```

```python
path = []
used = [0] * 7 # 전역 리스트를 사용(used 배열 or visited 배열)

def KFC(x):
    if x == 3:
        print(path)
        return

    for i in range(1, 7):
        # 중복 X : i가 이미 뽑혔다면, continue 해라
        # 아래 코드의 단점 : "in" = 0(len(path))
        # # !!! 시간 초과 위험도가 높다 !!!
        # if i in path:
        #     continue

        if used[i] == 1: # if not used[i]와 동일한 결과 출력
            continue

        used[i] = 1
        path.append(i)
        KFC(x+1)
        path.pop()
        used[i] = 0

KFC(0)
```

### 완전 탐색(Brute-Force, 브루트 포스 알고리즘):

모든 가능한 경우를 모두 시도하여 정답을 찾아내는 알고리즘