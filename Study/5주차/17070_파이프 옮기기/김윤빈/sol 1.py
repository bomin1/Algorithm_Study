import sys

input = sys.stdin.readline


# sys.stdin = open('input.txt')
# T = int(input())


def dfs(r, c, mode):
    # print(visited)
    global ans
    # mode 0 가로
    # mode 1 세로
    # mode 2 대각선

    if r == N - 1 and c == N - 1:
        ans += 1
        return

    # 가로로 가기
    if mode == 0 or mode == 2:
        nr = r
        nc = c + 1
        if 0 <= nr < N and 0 <= nc < N and not pipe[nr][nc]:
            dfs(nr, nc, 0)

    # 세로로 가기
    if mode == 1 or mode == 2:
        nr = r + 1
        nc = c
        if 0 <= nr < N and 0 <= nc < N and not pipe[nr][nc]:
            dfs(nr, nc, 1)

    # 대각선으로 가기
    if mode == 0 or mode == 1 or mode == 2:
        nr = r + 1
        nc = c + 1
        if 0 <= nr < N and 0 <= nc < N and not pipe[nr][nc] and not pipe[r][c + 1] and not pipe[r + 1][c]:
            dfs(nr, nc, 2)


# for tc in range(1, T + 1):
N = int(input())
pipe = [list(map(int, input().split())) for _ in range(N)]


# mode 가로 세로 대각선
# 가로 > 가로 , 대각선
# 세로 > 세로 , 대각선
# 대각선 > 가로,세로,대각선

ans = 0

dfs(0, 1, 0)
print(ans)
