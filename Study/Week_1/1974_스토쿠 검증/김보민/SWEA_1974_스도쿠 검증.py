import sys
sys.stdin = open("input.txt")

T = int(input())
# 카운팅 정렬 사용
def sudoku(arr):
    # 가로 판별
    for i in range(9):
        cnt = [0] * 10
        for ele in arr[i]:
            cnt[ele] += 1
            # 각 숫자 카운트한게 1보다 크면 두개 들어있으니까 xxxxxxx
            if cnt[ele] > 1:
                return 0
    # 세로 판별
    for j in range(9):
        cnt = [0] * 10
        for i in range(9):
            cnt[arr[i][j]] += 1
            if cnt[arr[i][j]] > 1:
                return 0

    # 3*3 판별
    for i in range(0,9,3):
        for j in range(0,9,3):
            cnt = [0] * 10
            for row in range(3):
                for col in range(3):
                    cnt[arr[i+row][j+col]] += 1
                    if cnt[arr[i+row][j+col]] > 1:
                        return 0
    return 1



for tc in range(1, T+1):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))

    su = sudoku(arr)

    print("#{} {}".format(tc, su))

