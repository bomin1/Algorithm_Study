import sys

# sys.stdin = open('input.txt')

from collections import deque

N, M = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(M)]

visited = [[0 for _ in range(N)] for _ in range(M)]
# print(tomato)

start = []
tomato_flag =False
for i in range(M):
    for j in range(N):
        if tomato[i][j] == 1:
            start.append([i, j])
        if tomato[i][j] == -1:
            visited[i][j] = -1
        if tomato[i][j] == 0 :
            tomato_flag = True

queue = deque()
for i in range(len(start)):
    queue.append(start[i])

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

        if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and not tomato[nr][nc]:
            visited[nr][nc] = visited[r][c] + 1
            queue.append([nr, nc])

for i in range(len(start)):

    visited[start[i][0]][start[i][1]] = 1

result = 0
flag =False
if tomato_flag:
    for i in range(M):
        for j in range(N):
            if visited[i][j] ==0:
                flag = True
                print(-1)
                break
            result = max(visited[i][j], result)
        if flag:
            break
    else:
        print(result)
else:
    print(0)