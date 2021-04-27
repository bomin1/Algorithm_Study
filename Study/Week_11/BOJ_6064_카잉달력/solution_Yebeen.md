# 6064. 카잉달력

처음에 생각한 코드

```python
from math import gcd
def lcm(x,y):
    return x*y // gcd(x,y)
T = int(input())
for tc in range(1,T+1):
    M,N,x, y = map(int, input().split())
    result = -1
    # x에 맞춰서 나머지 x일 때를 시작부터 M만큼 주기로 반복
    #나머지가 x인 수들만 N으로 나눠서 나머지가 y인것 찾아냄
    # 10 12 3 9 일 때 3,13,23,33 에서 12로 나눴을 때 9인것 찾아냄
    for num in range(x,lcm(N,M)+1,M):
        if num % N == y:
            result = num
            break
    print(result)
```

M를 기준으로 나머지가 x 인 것만을 최소 공배수까지 반복문을 돌려보면서 N으로 나눴을 때 나머지가 y인 숫자를 출력하는 것으로 짰는데 자꾸 테스트케이스가 틀렸다고 떴다.

그래서 하도 모르겠어서 인터넷에 검색해보니까 x=x-1,y=y-1을 하고 시작하더라.

처음에 왜 그래야하는지 정말 몰랐다. 몇 시간을 써서 알아낸 결과(진짜 오래걸렸다..ㅡㅡ)

원래의 나머지로 구하면 10(M)으로 나눴을 때는 1 2 3 4 5 6 7 8 9 0이다. 그런데 이 문제에서는  1 2 3 4 5 6 7 8 9 10으로 된다. 0이 아니라 10이다. 그래서 처음에 x = x-1 y= y-1로 바꿔주고 값을 찾았을 때 +1을 해서 출력해준다.

```python
from math import gcd
def lcm(x,y):
    return x*y // gcd(x,y)
T = int(input())
for tc in range(1,T+1):
    M,N,x, y = map(int, input().split())
    result = -1
    x = x-1
    y = y-1
    for num in range(x,lcm(N,M)+1,M):
        if num % N == y:
            result = num +1
            break
    print(result)
```