import sys

sys.stdin = open('input.txt')

T = 10

for _ in range(1, T + 1):
    tc = int(input())

    pw = list(map(int, input().split()))

    result = 0

    while True:
        # 0번 인덱스 빼기
        now = pw.pop(0)
        # 감소할 숫자 1~5까지 한사이클
        result += 1
        # 0번인덱스에 숫자를 빼서 append
        pw.append(now - result)
        # 빼줬을때 0이하면 break
        if pw[-1] <= 0:
            pw[-1] = 0
            break
        # 사이클 반복을 위한 count 설정
        if result == 5:
            result = 0
    print("#{}".format(tc), end=' ')
    print(*pw)
