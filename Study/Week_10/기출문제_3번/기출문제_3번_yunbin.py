import sys

sys.stdin = open('input.txt')

T = int(input())


def bfs(r, c):
    # vistied를 여러번 사용할꺼라 초기화를 안에서 시켜줌 
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # bfs 로직
    queue = [[r, c]]
    while queue:
        now = queue.pop(0)
        r = now[0]
        c = now[1]
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                queue.append([nr, nc])
                # bfs를 하면서 존을 찾으면 존까지 이동거리와, 찾은 존의 좌표를 리턴 
                if maze[nr][nc] == 3 or maze[nr][nc] == 4 or maze[nr][nc] == 5 :
                    return visited[nr][nc], [nr, nc]


for tc in range(1, T+1):
    N = int(input())
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    maze = [list(map(int, input().split())) for _ in range(N)]

    # 로봇 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_r = i
                start_c = j
                break
    ans = 0
    count = 0

    # 존을 세개 찾아야하므로 

    for i in range(3):

        # 존의 이동거리, 찾은 존의 좌표 리턴 
        result, now = bfs(start_r, start_c)


        # 찾은 존에서 부터 다시 bfs 시작 
        start_r = now[0]
        start_c = now[1]
        # 찾은 존은 다시 못들어가게 1로 바꿔서 벽으로 인식 
        maze[start_r][start_c] =1
        ans += result
    print("#{} {}".format(tc, ans))
