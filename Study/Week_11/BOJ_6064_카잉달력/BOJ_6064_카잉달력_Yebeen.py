from math import gcd
def lcm(x,y):
    return x*y // gcd(x,y)
T = int(input())
for tc in range(1,T+1):
    M,N,x, y = map(int, input().split())
    result = -1
    x = x-1
    y = y-1

    # x에 맞춰서 나머지 x일 때를 시작부터 M만큼 주기로 반복
    #나머지가 x인 수들만 N으로 나눠서 나머지가 y인것 찾아냄
    # 10 12 3 9 일 때 3,13,23,33 에서 12로 나눴을 때 9인것 찾아냄
    for num in range(x,lcm(N,M)+1,M):
        if num % N == y:
            result = num +1
            break
    print(result)
