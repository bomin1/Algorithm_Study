[toc]

# 20364_부동산 다툼

> Silver 2



## 문제

이진 트리 모양의 땅으로 이루어진 꽉꽉마을에는 오리들이 살고 있다. 땅 번호는 다음과 같이 매겨진다.

1. 루트 땅의 번호는 1이다.
2. 어떤 땅의 번호가 *K*라면, 왼쪽 자식 땅의 번호는 2 × *K*, 오른쪽 자식 땅의 번호는 2 × *K* + 1이다.

어느날 오리들끼리 부동산 다툼이 일어나서 꽉꽉마을 촌장 경완이가 해결책을 가져왔고, 그 내용은 다음과 같다.

1. 오리들을 한 줄로 대기시킨다. 맨 처음 오리들은 1번 땅에 위치해 있다.
2. 오리들이 서있는 순서대로 원하는 땅을 가지도록 한다.

![img](README.assets/preview)

만약, 한 오리가 원하는 땅까지 가는 길에 이미 다른 오리가 점유한 땅이 있다면 막대한 세금을 내야 하는 이유로 해당 땅을 지나가지 못해 그 오리는 땅을 가지지 못한다. 오리가 원하는 땅까지 가는 길에는 오리가 원하는 땅도 포함된다.



경완이의 해결책대로 땅 분배를 했을 때 각 오리별로 원하는 땅을 가질 수 있는지, 가질 수 없다면 처음 마주치는 점유된 땅의 번호를 구해보자.

### 입력

첫 번째 줄에 땅 개수 *N*과 꽉꽉나라에 사는 오리 수 *Q*가 공백으로 구분되어 주어진다. (2 ≤ *N* < 220, 1 ≤ *Q* ≤ 200,000)

두 번째 줄부터 차례로 *Q*개의 줄에 걸쳐 *i*+1번째 줄에는 *i*번째 오리가 원하는 땅 번호 *xi*가 주어진다. (2 ≤ *xi* ≤ *N*)

### 출력

*Q*개의 줄에 원하는 땅에 갈 수 있다면 0을, 갈 수 없다면 처음 마주치는 점유된 땅의 번호를 출력한다.

### 예제 입력 1

```
6 4
3
5
6
2
```

### 예제 출력 1

```
0
0
3
0
```





## 풀이과정



초반에는 다음과 같이 풀려고 했다.

```python
N, Q = map(int, input().split())

ducks = [int(input())for _ in range(Q)]

tree = [0 for _ in range(N + 1)]

def go_duck(n):
    global fail
    if tree[n] == 1:
        return n
    else:
        if n == duck:
            tree[duck] = 1
            return 0
        else:
            if n*2 <= N:
                go_duck(2*n)
            if n*2+1 <= N:
                go_duck(2*n+1)

for i in range(Q):
    duck = ducks[i]
    fail = 0
    go_duck(1)
    print(fail)
    print(go_duck(1))
print(tree)
```

하지만 재귀함수를 잘 이해하지 못했던 것 같다 당연히 함수 호출이 자꾸 되니까 마지막으로 부른 함수가 return이 되는 과정이라서 아무것도 return 되지 않는데 하나의 함수를 쓸때처럼 착각한 것 같다.



그래서 방법을 바꾸기로 했다.





```python
import sys
sys.stdin = open('input.txt')

N, Q = map(int, input().split())

ducks = [int(input())for _ in range(Q)]

tree = [0 for _ in range(N + 1)]

visited = []

for i in range(Q):
    result = 0
    duck = ducks[i]
    visited.append(duck)
    while duck > 1:
        duck //= 2
        if duck in visited:
            result = duck
            break
    print(result)
```

역으로 원하는 곳에서 찾아서 들어가서 부모가 방문한 적이 있다면 결과를 출력하는 방식으로 하였더니 샘플 케이스는 똑같이 나왔으나 **시간초과**가 떴다....



```python
import sys
sys.stdin = open('input.txt')

N, Q = map(int, input().split())
ducks = [int(input())for _ in range(Q)]

# 방문 검사
visited = []

def go_duck(duck):
    # 와야하는길 탐색하기
    while duck > 1:
        duck //= 2
        # 누군가의 땅이라면 거기서 멈춰야 하므로 결과 정해짐
        if duck in visited:
            return duck
    visited.append(ducks[i])
    return 0


for i in range(Q):
    # 오리들 불러오기
    duck = ducks[i]
    print(go_duck(duck))   
```



뭐 이것저것 해봐도 시간초과가 뜬다... 



조원들의 도움을 받아 풀었다.







## 풀이

```python
N, Q = map(int, input().split())
ducks = [int(input())for _ in range(Q)]

# 방문 검사
visited = set()

for i in range(Q):
    result = 0
    # 오리들 불러오기
    duck = ducks[i]
    # 와야하는길 탐색하기
    while duck > 1:
        # 누군가의 땅이라면 거기서 멈춰야함
        # 하지만 거꾸로 거슬러 올라가기 때문에 가장 높은 조상을 계속 갱신
        if duck in visited:
            result = duck
        duck //= 2
    visited.add(ducks[i])


    print(result)
```

* 함수를 안쓰니까 시간 절약?
* 리스트 보다는 set으로 하니까 시간 절약