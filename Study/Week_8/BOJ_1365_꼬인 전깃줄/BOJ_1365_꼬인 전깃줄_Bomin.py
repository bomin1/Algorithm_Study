import sys
sys.stdin = open("input.txt")


def binary_search(pole, res):
    start = 0
    end = len(res)-1

    while start < end:
        mid = (start + end) // 2

        if res[mid] < pole:
            start = mid + 1
        else:
            end = mid
    if start == end:
        return start
    return -1

n = int(input())

poles = list(map(int, input().split()))
res = []

for pole in poles:
    if not res:
        res.append(pole)
    else:
        if res[-1] < pole:
            res.append(pole)
        else:
            idx = binary_search(pole, res)
            res[idx] = pole

print(n-len(res))