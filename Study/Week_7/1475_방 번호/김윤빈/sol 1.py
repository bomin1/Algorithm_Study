N = int(input())

number = {
    0: 1,
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 2,
    7: 1,
    8: 1,
}

count = 1

while N:
    # print(N)

    num = N % 10
    # print(num)
    if num == 9:
        num = 6

    number[num] -= 1
    # print(number)
    if number[num] < 0:
        count += 1
        for i in range(9):
            number[i] += 1
        number[6] += 1
        # print(number)

    N = N // 10
print(count)
