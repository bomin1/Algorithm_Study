import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    p,q = map(int, input().split())

    i = 1
    y_1_coor_order = [0]
    while True:
        tmp = i * (i + 1) // 2
        # print(tmp)
        y_1_coor_order.append(tmp)
        if tmp > 40000:
            break
        i += 1
    print(y_1_coor_order)


    for j in range(len(y_1_coor_order)):
        if p <= y_1_coor_order[j]:
            a = j - (y_1_coor_order[j] - p)
            b = 1 + (y_1_coor_order[j] - p)
            break
    print(a,b)

    for j in range(len(y_1_coor_order)):
        if q <= y_1_coor_order[j]:
            c = j - (y_1_coor_order[j] - q)
            d = 1 + (y_1_coor_order[j] - q)
            break
    print(c,d)

    print(a+c, b+d)

    res = y_1_coor_order[(a+c) + (b+d) -1] -(b+d-1)

    print("#{} {}".format(tc, res))
