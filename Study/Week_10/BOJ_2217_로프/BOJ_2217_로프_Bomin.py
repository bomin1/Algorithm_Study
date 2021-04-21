import sys
sys.stdin = open("input.txt")

T=1

for tc in range(1,T+1):
    n = int(input())
    weights = []
    for i in range(n):
        weights.append(int(input()))
    weights.sort(reverse=True)

    max_val = 0
    for idx in range(n):
        max_val = max(max_val, weights[idx] * (idx+1))
    print(max_val)


