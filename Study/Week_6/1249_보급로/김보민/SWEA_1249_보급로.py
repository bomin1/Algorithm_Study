import sys
import pprint
from _collections import deque
sys.stdin = open("input.txt")

T = int(input())
# 우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    # pprint.pprint(arr)
    # print(arr)

    ans = 0
    min = [[99999] * n for _ in range(n)]
    min[0][0] = 0

    q = deque()
    # 내 출발 위치 푸쉬
    q.append((0,0))


    while q:
        x,y = q.popleft()

        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]

            if 0 <= next_x < n and 0<= next_y< n:
                if min[x][y] + arr[next_x][next_y] < min[next_x][next_y]:
                    min[next_x][next_y]=min[x][y] + arr[next_x][next_y]
                    q.append((next_x, next_y))

    ans = min[-1][-1]




    print("#{} {}".format(tc, ans))

#     https://chanhuiseok.github.io/posts/algo-32/

