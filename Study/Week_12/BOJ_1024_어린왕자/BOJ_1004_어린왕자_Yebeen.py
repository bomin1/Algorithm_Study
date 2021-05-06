import math
import sys
input = sys.stdin.readline

T = int(input()) # 테케
# 행성계 진입/이탈 횟수를 최소화
for tc in range(T+1):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input()) # 행성계의 개수
    cnt = 0
    for i in range(n):
        temp = 0
        cx, cy, r = map(int, input().split()) # 행성계의 중점과 반지름
        # 행성 원 안에 시작점 or 도착점이 존재한다면 cnt += 1
        if (x1-cx)**2 + (y1-cy)**2 < r**2: # 시작점이 원안에 존재
            cnt += 1
            temp += 1
        if (x2-cx)**2+ (y2-cy)**2 < r**2: # 끝점이 원안에 존재
            cnt += 1
            temp += 1
        if temp == 2: # 시작점과 끝점이 같은 원 안에 있을 때는 temp == 2
            cnt -= 2 # 위에서 cnt 2를 더해줬으니까 뺀다

    print(cnt)