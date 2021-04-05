import sys
sys.stdin = open("input.txt")

T = int(input())
# 오-아-왼-위
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T+1):

    N = int(input())
    # N*N 배열 만들기
    snail = [[0] * N for _ in range(N)]
    # 초기 좌표
    x, y = 0, 0
    snail[x][y] = 1
    # dr, dc에 접근할 인덱스
    direction_idx = 0


    for i in range(2, N**2+1):
        # x,y 각각 dr, dc에 접근해서 해당 값 만큼 옮겨간 다음에 위치 변화해주기
        x += dr[direction_idx]
        y += dc[direction_idx]
        snail[x][y] = i

        # 좌표 값들이 범위를 안벗어나고 숫자가 아직 반영이 안되어있으면 위에 세줄 다시 시행
        if 0 <= x + dr[direction_idx] < N and 0 <= y + dc[direction_idx] < N and snail[x + dr[direction_idx]][y + dc[direction_idx]] == 0:
            continue
        # dr, dc가 원소가 4개 이므로.
        if direction_idx != 3:
            direction_idx += 1
        else:
            direction_idx = 0

    print('#{}'.format(tc))
    for i in snail:
        print(*i)

