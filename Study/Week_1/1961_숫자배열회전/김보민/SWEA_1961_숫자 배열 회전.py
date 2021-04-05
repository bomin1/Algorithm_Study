import sys
sys.stdin = open("input.txt")

T = int(input())
# 배열을 회전하는 함수 하나 만들기

def rot(arr):
    # 회전되어서 반환되는 리스트 = res
    # n*n 행렬이 0으로 모두 채워져 있는 상태
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[  j ][ n-1-i ] = arr[i][j]
    return res

for tc in range(1, T+1):
    n = int(input())
    # 숫자가 딱 붙어있으니까 int로 형변환하지 않고, 문자열 상태로 +해서 붙여주거나 아니면 join?
    arr = [list(input().split()) for _ in range(n)]
    arr_90 = rot(arr)
    arr_180 = rot(arr_90)
    arr_270 = rot(arr_180)
    print(arr_90)
    print(arr_180)

    print("#{} ".format(tc, ))
    for i in range(n):
        print("".join(arr_90[i]), "".join(arr_180[i]), "".join(arr_270[i]))



