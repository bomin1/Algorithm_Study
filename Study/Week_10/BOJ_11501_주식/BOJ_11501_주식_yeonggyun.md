[toc]

# BOJ 11501 주식

> Silver2



## 문제

홍준이는 요즘 주식에 빠져있다. 그는 미래를 내다보는 눈이 뛰어나, 날 별로 주가를 예상하고 언제나 그게 맞아떨어진다. 매일 그는 아래 세 가지 중 한 행동을 한다.

1. 주식 하나를 산다.
2. 원하는 만큼 가지고 있는 주식을 판다.
3. 아무것도 안한다.

홍준이는 미래를 예상하는 뛰어난 안목을 가졌지만, 어떻게 해야 자신이 최대 이익을 얻을 수 있는지 모른다. 따라서 당신에게 날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산을 해달라고 부탁했다.

예를 들어 날 수가 3일이고 날 별로 주가가 10, 7, 6일 때, 주가가 계속 감소하므로 최대 이익은 0이 된다. 그러나 만약 날 별로 주가가 3, 5, 9일 때는 처음 두 날에 주식을 하나씩 사고, 마지막날 다 팔아 버리면 이익이 10이 된다.

### 입력

입력의 첫 줄에는 테스트케이스 수를 나타내는 자연수 T가 주어진다. 각 테스트케이스 별로 첫 줄에는 날의 수를 나타내는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고, 둘째 줄에는 날 별 주가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다. 날 별 주가는 10,000이하다.

### 출력

각 테스트케이스 별로 최대 이익을 나타내는 정수 하나를 출력한다. 답은 부호있는 64bit 정수형으로 표현 가능하다.



## 풀이과정



SWEA 1859 백만장자 프로젝트 문제와 비슷하다 생각하여 동일한 방법으로 해봤다.

예제출력은 동일하게 나오지만  틀렸다고 나온다. 그러면 다른게 뭔지 찾아보자

```python
T = int(input())
# 매도 타이밍을 잡는 함수
def sell_point(price, start_idx):
    # 초기 고점은 시작 포인트로 잡자
    max_price = price[start_idx]
    # 고점이 오는 날짜 역시 시작 날짜
    max_idx = start_idx
    # 이익은 일단 0
    total = 0
    # price를 검토해서 최대값 생성
    for i in range(start_idx, len(price)):
        if price[i] > max_price:
            max_price = price[i]
            max_idx = i
    # 고점까지 매일 1씩 산 이득을 계산
    for i in range(start_idx, max_idx):
        total += max_price - price[i]
    # 만약 장이 마감됐다면, 즉 시작점이 끝점까지 왔다면
    if start_idx == len(price)-1:
        # 이제 끝
        return 0
    # 내가 고점에서 물리게 될거라면
    if max_idx == start_idx:
        # 하루 쉬자, 즉 한칸 넘어가자
        return sell_point(price, max_idx+1)
    # 최고점까지의 이득을 챙기고 그다음 고점 검토를 해보자
    return sell_point(price, max_idx) + total

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    result = sell_point(price,0)
    print("#{} {}".format(tc, result))

```

++ 런타임에러가 발생하였다. 아마 답이랑 과정은 맞는데 재귀로 풀다보니 지정한 재귀 깊이보다 깊어진 것 같다. 채점과정에서 90%가 넘었는데 못넘을걸 보고 추측하였다.😂







밑에와 같이 풀었더니 시간초과가 발생했다. 

while문에서 빠져나오지 않는 케이스가 존재하는 것 같다.

```python
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    result = 0
    idx = 0

    while True:
        if idx > len(price) - 1:
            break
        if price[idx] != max(price[idx: len(price)]):
            max_value = max(price[idx: len(price)])
            for i in range(idx, price.index(max_value)):
                result += max_value - price[i]
            idx = price.index(max_value) + 1
        else:
            idx += 1



    print("#{} {}".format(tc, result))
```



뒤에서 부터 도는 과정으로 새로 짜봤는데 이역시 틀리다고 나왔다.

```python
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    result = 0
    max_value = price[-1]
    for i in range(len(price)-1, -1, -1):
        if price[i] >= max_value:
            max_value = price[i]
        else:
            result += max_value - price[i]

    print("#{} {}".format(tc, result))
```







## 풀이

```python
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    
    # 기본원리
    # 뒤에서 부터 계산하며 맥스를 갱신해간다.
    # 맥스가 아닐경우는 이득이 되는 경우 이므로 현재 맥스값과 차이를 결과에 반영
    
    # 결과값 초기화
    result = 0
    # 뒤에서 부터 검사할것 이기 때문에 맨 뒤에 값을 맥스값 초기화
    max_value = price[-1]
    # 맨뒤부터 돌기
    for i in range(N-1, -1, -1):
        # 맥스값보다 크거나 같다면 -> 아무것도 안함 그냥 갱신
        if price[i] >= max_value:
            max_value = price[i]
        else:
            # 작다면 그것은 이득임
            result += max_value - price[i]
    
    print(result)
```

* SWEA 양식을 쓰다가 호되게 당했다. 출력이 다르게 나오니 맞은것도 틀릴수 밖에... 조심하자..