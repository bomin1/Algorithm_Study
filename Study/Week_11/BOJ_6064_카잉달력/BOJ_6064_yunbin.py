# -*- coding: utf-8 -*-
import sys

#
sys.stdin = open('input.txt')
T = int(input())


for tc in range(1, T + 1):
    M, N, x, y = map(int, input().split())
    x -= 1
    y -= 1
    k = x

    while k < N * M:
        if k % N == y:
            print(k + 1)
            break
        k += M

    if k % N != y:
        print(-1)