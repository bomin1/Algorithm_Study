import sys

sys.stdin = open('input.txt')

T = int(input())


def sudoko(sudo):
    for i in range(9):
        tp1 = []
        tp2 = []
        for j in range(9):
            tp1.append(sudo[i][j])
            tp2.append(sudo[j][i])
        if sum(tp1) != 45 or sum(tp2) != 45:
            return 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = []
            for x in range(3):
                for y in range(3):
                    temp.append(sudo[i+x][j+y])
            if sum(temp) != 45:
                return 0
    return 1


for tc in range(1, T + 1):
    sudo = [list(map(int, input().split())) for _ in range(9)]
    result = sudoko(sudo)
    print("#{} {}".format(tc, result))
