import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # n : 국가의 수, m : 비행기의 종류
    n,m = list(map(int, input().split()))

    for i in range(m):
        a,b = list(map(int, input().split()))

    print(n-1)