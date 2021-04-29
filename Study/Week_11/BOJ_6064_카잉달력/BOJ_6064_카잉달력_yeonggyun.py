import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    M, N, x, y = map(int, input().split())
    # 나머지 연산을 하기 위해 각각 -1 을 해준다.
    x -= 1
    y -= 1

    # 현재 검사할 년도를 x라고 지정한다.
    now = x

    # 현재 검사할 년도가 종말보다 크면 안됨
    while now < N * M:
        # 만약 검사 년도를 N으로 나눈 나머지가 y와 일치한다면
        # 찾던 년도 이므로
        if now % N == y:
            # 현재 검사 년도에 1을 더해줌
            print(now + 1)
            break
        # 아니라면 y의 다음 범위를 위해 M만큼 더해줌
        now += M
    # 이를했는데도 같지 않다면 해당 x
    if now % N != y:
        print(-1)

