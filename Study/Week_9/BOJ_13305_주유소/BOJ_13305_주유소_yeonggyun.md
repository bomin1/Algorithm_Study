[toc]





# 13305 주유소

> Silver 4







## 문제

어떤 나라에 N개의 도시가 있다. 이 도시들은 일직선 도로 위에 있다. 편의상 일직선을 수평 방향으로 두자. 제일 왼쪽의 도시에서 제일 오른쪽의 도시로 자동차를 이용하여 이동하려고 한다. 인접한 두 도시 사이의 도로들은 서로 길이가 다를 수 있다. 도로 길이의 단위는 km를 사용한다.

처음 출발할 때 자동차에는 기름이 없어서 주유소에서 기름을 넣고 출발하여야 한다. 기름통의 크기는 무제한이어서 얼마든지 많은 기름을 넣을 수 있다. 도로를 이용하여 이동할 때 1km마다 1리터의 기름을 사용한다. 각 도시에는 단 하나의 주유소가 있으며, 도시 마다 주유소의 리터당 가격은 다를 수 있다. 가격의 단위는 원을 사용한다.

예를 들어, 이 나라에 다음 그림처럼 4개의 도시가 있다고 하자. 원 안에 있는 숫자는 그 도시에 있는 주유소의 리터당 가격이다. 도로 위에 있는 숫자는 도로의 길이를 표시한 것이다. 

![img](README.assets/1.png)

제일 왼쪽 도시에서 6리터의 기름을 넣고, 더 이상의 주유 없이 제일 오른쪽 도시까지 이동하면 총 비용은 30원이다. 만약 제일 왼쪽 도시에서 2리터의 기름을 넣고(2×5 = 10원) 다음 번 도시까지 이동한 후 3리터의 기름을 넣고(3×2 = 6원) 다음 도시에서 1리터의 기름을 넣어(1×4 = 4원) 제일 오른쪽 도시로 이동하면, 총 비용은 20원이다. 또 다른 방법으로 제일 왼쪽 도시에서 2리터의 기름을 넣고(2×5 = 10원) 다음 번 도시까지 이동한 후 4리터의 기름을 넣고(4×2 = 8원) 제일 오른쪽 도시까지 이동하면, 총 비용은 18원이다.

각 도시에 있는 주유소의 기름 가격과, 각 도시를 연결하는 도로의 길이를 입력으로 받아 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소의 비용을 계산하는 프로그램을 작성하시오.

### 입력

표준 입력으로 다음 정보가 주어진다. 첫 번째 줄에는 도시의 개수를 나타내는 정수 N(2 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 인접한 두 도시를 연결하는 도로의 길이가 제일 왼쪽 도로부터 N-1개의 자연수로 주어진다. 다음 줄에는 주유소의 리터당 가격이 제일 왼쪽 도시부터 순서대로 N개의 자연수로 주어진다. 제일 왼쪽 도시부터 제일 오른쪽 도시까지의 거리는 1이상 1,000,000,000 이하의 자연수이다. 리터당 가격은 1 이상 1,000,000,000 이하의 자연수이다. 

### 출력

표준 출력으로 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용을 출력한다. 





## 풀이과정



초기에는 함수를 이용해 제일 낮은 가격의 주유소를 찾고

제일 낮은 가격의 주유소 뒤부터는 제일낮은 주유소가격 x 남은거리의 방식으로 접근하였고

제일 낮은 주유소 앞부터는 출발선부터 다시 낮은 가격을 찾고

제일 낮은 주유소가 출발선 바로 앞까지 왔다면 초기가격을 더해주고 함수를 종료하는 것을 실행하였다. 

```python
T = 2

def oil(idx):
    global total

    min_price = price[idx-1]
    min_idx = idx-1

    for i in range(idx):
        if price[i] < min_price:
            min_price = price[i]
            min_idx = i

    for i in range(min_idx, idx+1):
        total += price[min_idx] * distance[i]

    if min_idx == 1:
        total += price[0] * distance[0]
        return
    else:
        oil(min_idx)






for tc in range(T):
    N = int(input())
    distance = list(map(int, input().split()))
    price = list(map(int, input().split()))
    total = 0
    oil(len(distance)-1)
    print(total)
```

예제와는 동일하게 나왔는데 런타임 Recursion 에러가 발생하였다.





```python
import sys
sys.stdin = open('input.txt')

T = 2

for tc in range(T):
    N = int(input())
    distance = list(map(int, input().split()))
    price = list(map(int, input().split()))

    total = 0
    min_price = 1000000001
    min_idx = N
    while True:
        if min_idx == 0:
            break
        elif min_idx == 1:
            total += price[0] * distance[0]
            break
        else:
            for i in range(min_idx-1):
                if price[i] < min_price:
                    min_price = price[i]
                    min_idx = i

            for i in range(min_idx, N-1):
                total += price[min_idx] * distance[i]


    print(total)
```

이것도 마찬가지로 오류...







## 풀이

```python

N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

# 초기에는 무조건 첫 주유소에서 기름사서 가야함
total = distance[0] * price[0]
# 최솟값 설정
min_value = price[0]
# 실제 갈 거리 설정
d = 0

for i in range(1, N-1):
    # 싼 주유소를 찾았으면
    if price[i] < min_value:
        # 거리만큼 기름을 사자
        total += min_value * d
        # 싼곳의 가격
        min_value = price[i]
        # 거리 입력
        d = distance[i]
    else:
        # 싼곳이 아니라면 거리를 더해주자
        d += distance[i]
    
    # 마지막값은 제일 싼곳
    if i == N-2:
        total += min_value * d

print(total)


```

