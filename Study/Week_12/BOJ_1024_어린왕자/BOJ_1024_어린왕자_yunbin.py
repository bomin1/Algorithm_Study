import sys

# sys.stdin = open('input.txt')
# input = sys.stdin.readline
T = int(input())


def distance(d1x, d1y, d2x, d2y):
    return ((d1x - d2x) ** 2 + (d1y - d2y) ** 2) ** 0.5


for tc in range(1, T + 1):
    x1, y1, x2, y2 = map(int, input().split())

    N = int(input())
    count = 0
    for _ in range(N):
        cx, cy, r = map(int, input().split())

        if (distance(x1, y1, cx, cy) > r and distance(x2, y2, cx, cy) < r) or (
                distance(x1, y1, cx, cy) < r and distance(x2, y2, cx, cy) > r):
            count += 1
    print(count)
