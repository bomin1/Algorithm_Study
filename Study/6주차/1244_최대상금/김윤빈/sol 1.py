import sys

sys.stdin = open('input.txt')

T = int(input())


def dfs(number, start, count):
    # print(number, start, count)
    global result
    # 10개중 8개.. 뭐냐고  아아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ
    # 하면 답이 안나오고.....

    # if result > int(''.join(number)):
    #     return

    if int(count) == 0:
        if result < int(''.join(number)):
            result = int(''.join(number))
        return

    for i in range(start, N):
        for j in range(i + 1, N):
            if number[i] <= number[j]:
                number[i], number[j] = number[j], number[i]
                dfs(number, i, int(count) - 1)
                number[i], number[j] = number[j], number[i]


# T = 1
for tc in range(1, T + 1):
    num, cnt = map(str, input().split())
    num = list(num)
    N = len(num)

    # 예외 처리 > 21 과같이 이미 큰수를 줘버렸을때(역수일때가 가장 크니까)
    if len(num)==2 or num == sorted(num, reverse=True):
        c = 0
        while c != int(cnt):
            num[-1],num[-2] = num[-2],num[-1]
            c += 1

        expect = num
    result = 0

    dfs(num, 0, cnt)
    # print(visited)
    if result == 0:
        result= ''.join(expect)
    print("#{} {}".format(tc, result))
