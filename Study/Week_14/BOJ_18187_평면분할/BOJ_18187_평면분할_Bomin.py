import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    res = 0
    i = 1
    for j in range(n + 1):
        res += i
        if j % 3 != 0:
            i += 1

    print(res)


