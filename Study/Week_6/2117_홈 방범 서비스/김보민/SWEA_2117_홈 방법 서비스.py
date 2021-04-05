import sys
import pprint
sys.stdin = open("input.txt")


T = int(input())

def cal(i,j):
    cnt = 0
    for x,y in houses:
        if abs(x-i) + abs(y-j) < k:
            cnt += 1
    return cnt*m,cnt


for tc in range(1, T+1):
    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    houses = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                houses.append((i,j))

    # print(houses)

    max_house = 1

    for i in range(n):
        for j in range(n):
            for k in range(1,2*n):
                cost = k * k + (k - 1) * (k - 1)
                check_cost,house_cnt = cal(i, j)
                if check_cost >= cost and house_cnt > max_house:
                    max_house = house_cnt

    print('#{} {}'.format(tc, max_house))
