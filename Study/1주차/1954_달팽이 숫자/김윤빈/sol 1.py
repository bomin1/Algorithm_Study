import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # 시계방향
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 방향제어를 위한 mode 설정
    mode = 0
    # 초기점 row col = r, c(0,0)
    r = 0
    c = 0
    # 정사각형의 크기
    N = int(input())

    # N*N 리스트 만들기
    snail = [[0] * N for _ in range(N)]

    # 초기화
    snail[r][c] = 1
    for i in range(2, N * N + 1):

        # 방향을 바꾸는지 체크하기
        # 그다음 스텝 기준을 생각해보자
        # 1. row가 박스안에 들어가있는지
        # 2. col이 박스안에 들어가있는지
        # 3. 그다음 스텝을 밟았을때 지나가지않은 상자인지?
        # 모두 충족한다면 좌표를 바꾸지않는다.
        if 0 <= r+dr[mode] < N and 0 <= c+dc[mode] < N and not snail[r+dr[mode]][c+dc[mode]]:
            # 스텝을 밟기 위한 좌표 설정
            nr = r + dr[mode]
            nc = c + dc[mode]
            # 좌표를 dr과 dc만큼 이동시켜놓은 nr nc를 바탕으로 이동 후 값을 넣어준다.
            snail[nr][nc] = i
            # 값을 바꾼 후 자신의 위치 변경
            r = nr
            c = nc
        else:
            # 만약 박스이탈, 그다음 스텝에 지나간 상자라면 경로를 바꾼다 .
            # mode +1 을 해주면 시계방향으로 설정한 dr dc를 보고 방향제어
            mode += 1
            # 4번만에 안끝나니까 %4로 나누어주면 4를 초과해도 한바퀴 돌아도 계속 돌아가게끔
            mode %= 4
            # 모드바꿨으니 달팽이의 발자취를 남겨주자
            nr = r + dr[mode]
            nc = c + dc[mode]
            snail[nr][nc] = i
            r = nr
            c = nc

    print("#{}".format(tc))
    # unpacking 연산자*
    # 이중리스트니까 풀어서 unpacking
    for i in range(N):
        print(*snail[i])
