from collections import deque

def bfs():
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # que가 존재할때 까지 검사
    while queue:
        # queue에서 좌표 받아옴
        x, y = queue.popleft()
        # 4개 방향 검사
        for i in range(4):
            # 현재 좌표를 cx, cy로 갱신시켜준다.
            cx = x + dx[i]
            cy = y + dy[i]
            # 만약 cx,cy가 범위 안에 있고 아직 익지 않은 것이었다면
            if 0 <= cx < N and 0 <= cy < M and tomato[cx][cy] == 0:
                # 토마토를 익혀준다. (자동으로 날짜가 들어가게 1을 더해줌)
                tomato[cx][cy] = tomato[x][y] + 1
                # 현재 익은 좌표를 넣어준다.
                queue.append([cx, cy])


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
# 초기의 익어있는 토마토 좌표를 큐에 넣어준다.
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])
# bfs를 실행한다.
bfs()

# 익지 못한 토마토를 발견했을 경우를 검사하기 위한 변수 초기화
check = 0
# 모두 익어있다면 1만 더해질것 이므로 초기값 -2로 설정
result = -2
for i in range(N):
    for j in range(M):
        # 익지 않은 토마토가 있다면 체크해줌
        if not tomato[i][j]:
            check = 1
        # 결과값이 더 큰 값이 나온다면 갱신해줌
        if tomato[i][j] > result:
            result = tomato[i][j]
# 만약 익지 못한 토마토가 있으면 -1
if check:
    print(-1)
# 애초부터 익어있던 상황이라면 -1이 나오게 될 것임
elif result == -1:
    print(0)
# 그외의 경우에는 최대값에서 -1을 해준값이 최소날짜가 될 것 이다.
else:
    print(result-1)