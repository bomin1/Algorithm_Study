import sys

sys.stdin = open('input.txt')
T = int(input())


def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return
    # 1번기둥+2번기둥+3번기둥 = 6
    # 보조기둥 찾는 방법, 6- 현재 기둥-목표기둥

    hanoi_tower(n - 1, start, 6 - start - end)  # 1단계 n-1번까지 보조기둥으로 옮기는 작업
    print(start, end)  # 2단계 n번을 원하는 기둥으로 옮기고
    hanoi_tower(n - 1, 6 - start - end, end)  # 3단계 보조기둥으로 옮긴 친구들을 원하는 기둥으로 옮기는 작업



for tc in range(1, T + 1):


    n = int(input())
    print(2 ** n - 1)
    hanoi_tower(n, 1, 3)