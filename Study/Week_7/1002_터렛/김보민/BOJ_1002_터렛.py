import math
import sys
sys.stdin = open("input.txt")

T = int(input())

def cal():
    # 두 원이 겹칠 때 -> 무수히 많음 -> -1
    if d == 0 and r1==r2:
        return -1
    # 두 원이 밖으로 떨어져 있을 때 -> 겹치는 부분이 없음 -> 0
    # 작은 원이 큰 원 안에 있는데 둘이 겹치지 않는 경우
    elif (d > r1+r2) or (d < abs(r1-r2)):
        return 0
    # 외접 or 내접
    elif (d == r1+r2) or (d == abs(r1-r2)):
        return 1
    else:
        return 2

for tc in range(1,T+1):
    '''
    조규현의 좌표 (x1, y1)
    백승환의 좌표 (x2, y2)
    조규현이 계산한 류재명과의 거리 r1과
    백승환이 계산한 류재명과의 거리 r2
    '''
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    # d = 중점 사이의 거리
    d = math.sqrt(pow((x1 - x2),2) + pow((y1 - y2),2))

    res = cal()
    print(res)

