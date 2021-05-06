import sys
sys.stdin = open("input.txt")

T=int(input())
for tc in range(1, 1+T):
    n = int(input())
    t = []
    p = []
    res = [0 for i in range(n+1)]

    for i in range(n):
        x,y = map(int, input().split())
        t.append(x)
        p.append(y)

    for i in range(n-1,-1,-1):
        if i + t[i] > n:
            res[i] = res[i+1]
        else:
            res[i] = max(res[i+1], p[i] + res[i+t[i]])

    print(res[0])