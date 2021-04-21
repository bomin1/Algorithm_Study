import sys
sys.stdin = open("input.txt")

T=int(input())

for tc in range(1,T+1):
    n = int(input())
    costs = list(map(int, input().split()))

    max_val = costs[-1]
    res = 0
    for i in range(n-2,-1,-1):
        max_val = max(costs[i], max_val)
        if costs[i] < max_val:
            res += max_val-costs[i]

    print(res)