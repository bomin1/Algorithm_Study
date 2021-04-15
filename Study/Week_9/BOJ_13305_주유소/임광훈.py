n = int(input())
road = list(map(int, input().split()))
gas = list(map(int, input().split()))

mymin = gas[0]
dis = 0
price = 0

for i in range(n-1):
    if gas[i] <= mymin:
        price += mymin*dis
        mymin = gas[i]
        dis = road[i]
    else:
        dis += road[i]

price += mymin*dis
print(price)