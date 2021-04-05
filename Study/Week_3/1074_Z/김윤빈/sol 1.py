import sys

sys.stdin = open('input.txt')
T = int(input())


def z(size, x, y):
    global cnt
    # 2x2 행렬까지 쪼개졌을때
    if size == 2:
        if x == r and y == c:
            print(cnt)
            return
        cnt += 1
        if x == r and y + 1 == c:
            print(cnt)
            return
        cnt += 1
        if x == r and y + 1 == c:
            print(cnt)
            return
        cnt += 1
        if x + 1 == r and y + 1 == c:
            print(cnt)
            return
        cnt += 1
    else:
        z(size // 2, x, y)
        z(size // 2, x, y + size // 2)
        z(size // 2, x + size // 2, y)
        z(size // 2, x + size // 2, y + size // 2)
    pass


for tc in range(1, T + 1):
    n, r, c = map(int, input().split())

    cnt = 0
    z(2 ** n, 0, 0)
