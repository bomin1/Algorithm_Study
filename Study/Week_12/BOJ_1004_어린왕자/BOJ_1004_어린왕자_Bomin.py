import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 출발점, 도착점
    x1,y1,x2,y2 = list(map(int, input().split()))
    # 행성의 갯수
    n = int(input())
    cnt = 0
    for i in range(n):
        cx, cy, r = list(map(int, input().split()))
        ds = (x1-cx) * (x1-cx) + (y1-cy) * (y1-cy)
        de = (x2-cx) * (x2-cx) + (y2-cy) * (y2-cy)

        if (ds<r*r) and (de < r*r):
            continue
        elif (ds<r*r) or (de < r*r):
            cnt += 1
    print(cnt)


