import sys
import math
input = sys.stdin.readline
# sys.stdin = open('input.txt')

T = int(input())


def is_prime_number(x):
    for j in range(2, int(math.sqrt(x)) + 1):
        if x % j == 0:
            return False
    return True


for tc in range(1, T + 1):
    N = int(input())
    result = []
    for i in range(N // 2, 1, -1):

        if is_prime_number(i) and is_prime_number(N - i):
            result.append([i,N-i, (N-i-i)])

    result.sort(key= lambda x:x[2])
    print(result[0][0],result[0][1])