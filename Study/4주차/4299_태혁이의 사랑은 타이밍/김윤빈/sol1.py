import sys

sys.stdin = open('sample_input.txt')
T = int(input())


def day(D, H, M):

    today = (D - 11) * 60 * 24 + (H - 11) * 60 + M - 11
    if today < 0:
        return -1
    else:
        return today


for tc in range(1, T + 1):
    # D (11 ≤ D ≤ 14), H (0 ≤ H ≤ 23), M (0 ≤ M ≤ 59)
    D, H, M = map(int, input().split())

    print("#{} {}".format(tc, day(D, H, M)))
