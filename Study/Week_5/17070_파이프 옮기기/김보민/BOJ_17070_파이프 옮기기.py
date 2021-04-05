import sys
sys.stdin = open("input.txt")
import pprint

T=int(input())
# 가로 세로 대각선
dx = [0,1,1]
dy = [1,0,1]

# 파이스 상태 : 0-가로, 1-세로, 2-대각선
def bfs(x,y,pipe):
    global ans

    # 도착하면 끝
    if x == n-1 and y == n-1:
        ans += 1
        return

    # i : 가로 세로 대각선 각각 해보기
    for pipe_shape in range(3):
        # 가로일때는 세로 안되고 세로일때는 가로안됨
        if (pipe_shape==0 and pipe == 1) or (pipe_shape == 1 and pipe == 0):
            continue

        next_x = x + dx[pipe_shape]
        next_y = y + dy[pipe_shape]

        # 벽이거나 범위 넘어가거나
        if next_x>=n or next_y>=n or arr[next_x][next_y] == 1:
            continue

        # 지금 파이프가 대각선일때
        if pipe_shape == 2 and (arr[x][y+1] == 1 or arr[x+1][y] == 1 or arr[x+1][y+1] == 1):
            continue

        bfs(next_x,next_y,pipe_shape)



for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    pprint.pprint(arr)
    ans = 0
    bfs(0,1,0)

    print(ans)



