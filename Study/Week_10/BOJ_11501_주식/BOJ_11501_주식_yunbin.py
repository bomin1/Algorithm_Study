import sys
sys.stdin = open('input.txt')
T = int(input())

for _ in range(1,T+1):

    N = int(input())

    stock = list(map(int,input().split()))[::-1]

    result = 0
    fee = stock[0]

    for i in range(1,len(stock)):
        if stock[i] < fee:
            result += (fee-stock[i])
        else:
            fee = stock[i]

    print(result)


    