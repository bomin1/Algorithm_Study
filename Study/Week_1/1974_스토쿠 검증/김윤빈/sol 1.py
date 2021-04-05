import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    sudo = []
    for i in range(9):
        line = list(map(int, input().split()))
        sudo.append(line)
    # print(sudo)
    # [[7, 3, 6, 4, 2, 9, 5, 8, 1], [5, 8, 9, 1, 6, 7, 3, 2, 4], [2, 1, 4, 5, 8, 3, 6, 9, 7], [8, 4, 7, 9, 3, 6, 1, 5, 2], [1, 5, 3, 8, 4, 2, 9, 7, 6], [9, 6, 2, 7, 5, 1, 8, 4, 3], [4, 2, 1, 3, 9, 8, 7, 6, 5], [3, 9, 5, 6, 7, 4, 2, 1, 8], [6, 7, 8, 2, 1, 5, 4, 3, 9]]

    result = 1
    # 1. 가로 체크
    for i in range(len(sudo)):
        temp = 0
        for j in range(len(sudo)):
            temp += sudo[i][j]
        if temp != 45:
            result = 0
            break

    # 2. 세로 체크
    for i in range(len(sudo)):
        temp = 0
        for j in range(len(sudo)):
            temp += sudo[j][i]
        if temp != 45:
            result = 0
            break
    # 3. 3x3 체크
    """
    3개씩 나눠서 체크하는게 어렵다 4중 포문.. 이게 맞나?
    """

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = 0
            for x in range(3):
                for y in range(3):
                    temp += sudo[i + x][j + y]
            if temp != 45:
                result = 0
                break
    print("#{} {}".format(tc, result))
