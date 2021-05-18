# 토마토 

## 문제

철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. 

![img](https://www.acmicpc.net/upload/images/tmt.png)

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

## 입력

첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

## 출력

여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

## 예제 입력 1 복사

```
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
```

## 예제 출력 1 복사

```
8
```



## 풀면서 느낀점

2차원배열에 최소 일수를 구하는 문제이기떄문에 bfs로 풀어야겠다고 생각했다. 

**토마토가 하나 이상 있는 경우만 입력으로 주어진다.** 을 보고 스타팅 포인트가 2개이상일 수 있으니까 스타트포인트를 모두 찾아서 큐에 집어넣야된다고 생각했다. 

어차피 한번은 for문을 돌기에 돌때, **저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고** 의 조건을 보고 0을 한번 보면 flag값을 주고 조건을 주는 방법을 생각했다.



## 나의 코드

```python
import sys

# sys.stdin = open('input.txt')

from collections import deque

N, M = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(M)]

visited = [[0 for _ in range(N)] for _ in range(M)]
# print(tomato)

queue = deque()
start = []
tomato_flag =False
for i in range(M):
    for j in range(N):
      	# start_point
        if tomato[i][j] == 1:
            queue.append([i, j])
            start.append([i,j]) # 모두 방문했는지 체크하기 스타팅 저장 
        if tomato[i][j] == -1:
            visited[i][j] = -1 # 모두 방문했는지 체크하기 위해 -1 체크
        # 0이 없으면 모두 익은 상태 
        if tomato[i][j] == 0 :
            tomato_flag = True


 
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

result = 0
while queue:
    now = queue.popleft()
    r, c = now[0], now[1]
    # print(r,c)

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
				# 1. 맵안에 있기 2. 방문하지 않은 곳 3. 토마토가 익지 않은 곳 
        if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and not tomato[nr][nc]:	
            visited[nr][nc] = visited[r][c] + 1 # bfs
            queue.append([nr, nc])
# 스타팅 포인트 1로 넣기 
for i in range(len(start)):

    visited[start[i][0]][start[i][1]] = 1

result = 0
flag =False
# 
# 이미 익어있는 상태인지 체크 
if tomato_flag:
    for i in range(M):
        for j in range(N):
          	# 아직 익지않은 복숭아가 있다면  -1 break
            if visited[i][j] ==0:
                flag = True
                print(-1)
                break
            # 아니라면 가장 큰 값 갱신 
            result = max(visited[i][j], result)
        if flag:
            break
    # break를 걸리지 않았다면 result 출력 
    else:
        print(result)
else:
    print(0)
```



