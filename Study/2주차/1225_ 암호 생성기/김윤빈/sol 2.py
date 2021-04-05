import sys
from collections import deque

sys.stdin = open('input.txt')
T = 10

for _ in range(1, T + 1):

    tc = int(input())

    numbers = list(map(int, input().split()))
    # print(numbers)
    dq = deque(numbers)
    # print(dq.popleft())
    result = 0
    while True:
        now = dq.popleft()

        result += 1

        dq.append(now - result)
        if dq[-1] <= 0:
            dq[-1] = 0
            break

        if result == 5:
            result = 0

    print("#{}".format(tc), end=' ')
    print(*dq)
