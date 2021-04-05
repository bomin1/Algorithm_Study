import sys
import math

sys.stdin = open('input.txt')

T = int(input())


def distance_point(x_1, y_1, x_2, y_2):
    return math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)


for tc in range(1, T + 1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    r = distance_point(x1, y1, x2, y2)

    if r == 0:
        # 포개어져 있을때
        if r1 == r2:
            result = -1
        # 좌표가 같은데 반지름 크기가다르면 절대 못만남
        else:
            result = 0

    # 좌표가 다를때
    else:
        # 한점에서 만나는 경우 외접/ 내접
        if r == r1 + r2 or r == abs(r1 - r2):
            result = 1
        # 못만나는 경우
        elif r > r1 + r2 or r1 > r + r2 or r2 > r + r1:
            result = 0
        else:
            result = 2
    print(result)
