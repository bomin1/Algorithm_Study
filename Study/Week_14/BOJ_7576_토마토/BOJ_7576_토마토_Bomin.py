import sys
sys.stdin = open("input.txt")
from collections import deque

T = int(input())

dx = [0, 1, 0 ,-1]
dy = [1, 0, -1, 0]

def bfs(box,q):
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            elif box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append((nx,ny))


for tc in range(1, T+1):
    m,n = list(map(int, input().split()))
    box = [list(map(int, input().split())) for _ in range(n)]
    q = deque()
    # print(m,n)
    # print(box)

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                q.append((i,j))
    bfs(box, q)

    cnt = 0

    for i in range(n):
        if 0 in box[i]:
            cnt = 0
            break
        else:
            cnt = max(cnt,max(box[i]))
    print(cnt-1)


