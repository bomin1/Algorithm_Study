import sys
sys.stdin = open("input.txt")

# n : 도시의 갯수
n = int(input())
distance = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

min_price = 1000000000
res = 0

for i in range(n-1):
    min_price = min(min_price, oil_price[i])
    res += min_price * distance[i]

print(res)



