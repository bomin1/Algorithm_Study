import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    money = int(input())
    five, two, cnt = 0, 0, 0
    if money == 1 or money == 3:
        cnt = -1
    else:
        five = money // 5
        money %= 5
        if money == 1:
            five -= 1
            two += 3
        elif money == 2:
            two += 1
        elif money == 3:
            five -= 1
            two += 4
        elif money == 4:
            two += 2
        cnt = five + two
    print(cnt)


