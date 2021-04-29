# 촌수계산 

## 문제

우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

## 입력

사람들은 1, 2, 3, …, n (1≤n≤100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.

## 출력

입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.

## 예제 입력 1 

```
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
```

## 예제 출력 1 

```
3
```



## 풀면서 느낀점

촌수 계산에서 주어진 인풋값이 그래프 형태로 들어오는 형태여서 엣지리스트나 엣지 매트릭스로 그래프를 표현한뒤에 dfs나 bfs로 방문을 안한 노드를 찾아보면 되겠다라고 생각했다. 

일단 인풋값을 받아오면서 엣지리스트로 받아오는게 더 편해서 인풋값을 받은뒤에 bfs로 노드를 방문처리해주면서 count를 매겨줬다. 그렇게 queue가 모두 끝났는데도 답이 없다면 -1을 출력하도록 해줬다. 



## 나의 코드

```python
import sys
from collections import deque

# sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())

start, end = map(int, input().split())

M = int(input())

edge_list = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for i in range(M):
    parent, child = map(int, input().split())
    edge_list[parent].append(child)
    edge_list[child].append(parent)

# print(edge_list)
# [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]

visited[start] = True
queue = deque()
queue.append([start, 0])

while queue:
    now, count = queue.popleft()

    if now == end:
        print(count)
        break
    count += 1
    for i in edge_list[now]:
        if not visited[i]:
            visited[i] = True
            queue.append([i, count])
else:
    print(-1)

```

