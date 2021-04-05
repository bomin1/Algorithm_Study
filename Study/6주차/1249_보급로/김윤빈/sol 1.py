from collections import deque
import sys

sys.stdin = open('input.txt')
T = int(input())


def BFS(r, c):
    global result
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    queue = deque()
    queue.append([r, c])
    visited[r][c] = True

    while queue:
        row, col = queue.popleft()
        print(row,col)
        # 4방향 탐색
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            # 1. 맵안에 nr이 있어야한다.
            # 2. 방문하지 않은 곳
            # 3. 최소거리???????? 어케함
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    distance[nr][nc] = distance[r][c] + load[nr][nc]
                    queue.append([nr, nc])
        print(distance)


for tc in range(1, 2):
    N = int(input())
    load = [list(map(int, input())) for _ in range(N)]
    # BFS로 최단 거리 찾기?
    visited = [[False for _ in range(N)] for _ in range(N)]
    distance = [[0 for _ in range(N)] for _ in range(N)]
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited[0][0] = True

    result = 99999
    BFS(0, 0)
    print("#{} {}".format(tc, result))
