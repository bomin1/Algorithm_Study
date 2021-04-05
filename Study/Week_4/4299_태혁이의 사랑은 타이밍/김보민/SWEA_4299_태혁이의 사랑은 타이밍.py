import sys
sys.stdin = open("input.txt")

T = int(input())

def cal(d,h,m):
    ans = 0
    cal_d = d-11
    cal_h = h-11
    cal_m = m-11

    if d <11:
        return -1
    elif d == 11:
        if h < 11:
            return -1
        elif h == 11:
            if m == 11:
                return 0
        else:
            if m < 11:
                return -1
    else:
        ans = cal_m + (cal_h*60) +(cal_d*24*60)
        return ans

for tc in range(1, T+1):
    # 일, 분, 시
    d,h,m = map(int, input().split())
    res = cal(d, h, m)
    print("#{} {}".format(tc, res))

