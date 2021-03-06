# 2169_로봇 조종하기

> 다이나믹 프로그래밍



## 문제

NASA에서는 화성 탐사를 위해 화성에 무선 조종 로봇을 보냈다. 실제 화성의 모습은 굉장히 복잡하지만, 로봇의 메모리가 얼마 안 되기 때문에 지형을 N×M 배열로 단순화 하여 생각하기로 한다.

지형의 고저차의 특성상, 로봇은 움직일 때 배열에서 왼쪽, 오른쪽, 아래쪽으로 이동할 수 있지만, 위쪽으로는 이동할 수 없다. 또한 한 번 탐사한 지역(배열에서 하나의 칸)은 탐사하지 않기로 한다.

각각의 지역은 탐사 가치가 있는데, 로봇을 배열의 왼쪽 위 (1, 1)에서 출발시켜 오른쪽 아래 (N, M)으로 보내려고 한다. 이때, 위의 조건을 만족하면서, 탐사한 지역들의 가치의 합이 최대가 되도록 하는 프로그램을 작성하시오.



## 입력

첫째 줄에 N, M(1≤N, M≤1,000)이 주어진다. 다음 N개의 줄에는 M개의 수로 배열이 주어진다. 배열의 각 수는 절댓값이 100을 넘지 않는 정수이다. 이 값은 그 지역의 가치를 나타낸다.



## 출력

첫째 줄에 최대 가치의 합을 출력한다.

<br>

---

## Input

```txt
5 5
10 25 7 8 13
68 24 -78 63 32
12 -69 100 -29 -25
-16 -22 -57 -33 99
7 -76 -11 77 15
```

## Output

```
319
```

<br>

---

## Code

```python
import sys
sys.stdin = open("input.txt")

n,m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
test_arr = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]

res = [[0 for _ in range(m)] for _ in range(n)]
sum_val = 0

for i in range(m):
    sum_val += arr[0][i]
    res[0][i] = sum_val

for i in range(1,n):
    # 위에서 아래로
    for j in range(m):
        test_arr[i][j][0] = res[i-1][j] + arr[i][j]
        test_arr[i][j][1] = res[i-1][j] + arr[i][j]

    # 왼쪽에서 오른쪽으로 [ 0]번째
    for j in range(1,m):

        test_arr[i][j][0] = max(test_arr[i][j][0], test_arr[i][j-1][0] + arr[i][j])

    # 오른쪽에서 왼쪽으로 [1]번째
    for j in range(m-2,-1,-1):
        test_arr[i][j][1] = max(test_arr[i][j][1], test_arr[i][j+1][1] + arr[i][j])

    for j in range(m):
        res[i][j] = max(test_arr[i][j][0], test_arr[i][j][1])

print(res[-1][-1])
```



## Review

1. `res`는 탐사한 지역들의 가치의 합을 넣어줄 리스트이다.

2. 갈 수 있는 방법은 오른쪽으로 가기, 왼쪽으로 가기, 아래로 내려가기 이렇게 세 방향인데, 또 왔던 길은 다시 가면 안된다.

3. 그럼 첫번째 줄 같은 경우는 (1,1)에서 시작하니까 오른쪽으로 가는 방법 밖에 없다. 그래서 아래의 코드를 이용해서

   ```python
   for i in range(m):
       sum_val += arr[0][i]
       res[0][i] = sum_val
   ```

   res의 첫번째 행에 원래 값들을 더해주는 값을 넣어준다

   1 2 3 4 5 예를 들어 인풋 첫번째 행에 이런식으로 들어오면 res의 첫번째 행은

   1 3 6 10 15 이렇게 채워지는 경우이다 (오른쪽으로밖에 못가니까 이렇게만 넣어주면 끝)

4. 문제는 두번째 행부터인데, 

   ```python
   for i in range(1,n):
       # 위에서 아래로
       for j in range(m):
           test_arr[i][j][0] = res[i-1][j] + arr[i][j]
           test_arr[i][j][1] = res[i-1][j] + arr[i][j]
   ```

   i : 행, j : 열

   두번째 행부터 시작하면서 원래는 a,b로 값을 줘서 갱신하려고 했는데 그렇게 하면 왔던길을 다시 되돌아가고 이런것을 못해서 3차원 배열로 만들어줬다

   1 2 3 4 5

   10 9 8 7 6

   인풋이 이렇게 들어온다면 res는

   1 3 6 10 15 

   a,b,c,d,e

   이런 식으로 값이 들어와야하는데 a의 값을 아래, 오른쪽, 왼쪽을 보면서 제일 큰 값으로 갱신을 해줘야 하니까 우선 a 밑에 두개의 배열을 또 만들어줘서 그 두개의 배열에 아래로 움직일 때의 값을 넣어준다. 

5. 그 다음 왼쪽에서 오른쪽 방향으로 갈때 이미 아래쪽으로 이동할 때 계산된 값과 비교를 하면서 큰 값으로 갱신하면서 움직여야 하니까

   ```python
       # 왼쪽에서 오른쪽으로 [ 0]번째
       for j in range(1,m):
   
           test_arr[i][j][0] = max(test_arr[i][j][0], test_arr[i][j-1][0] + arr[i][j])
   ```

   아래로 이동한다 = (아래로 이동한다.)

   왼쪽에서 오른쪽으로 이동한다 = (아래로 이동한 다음 오른쪽으로 이동한다.)

   max(지금 아래로 이동한다= (아래로 이동한다.), 그 전에 아래로 이동한 다음(test_arr[i][j-1][0]) + 오른쪽으로 이동한다( arr[i][j]))

   이 두개 값 중 큰거 계산해서 갱신하기

6. 오른쪽에서 왼쪽으로 이동하는 거도 똑같이 위랑 같이 행동

   ```python
       # 오른쪽에서 왼쪽으로 [1]번째
       for j in range(m-2,-1,-1):
           test_arr[i][j][1] = max(test_arr[i][j][1], test_arr[i][j+1][1] + arr[i][j])
   ```

7. 그 다음에 아래로 이동하는건 이미 왼쪽으로 이동하는거랑 오른쪽으로 이동하는거에서 비교했기 때문에

   왼쪽이랑 오른쪽으로 이동하는거를 비교해서 제일 큰 값으로 res값 갱신

8. 이렇게 쭉 하다보면 res의 맨 마지막 값이 오른쪽 아래 (N, M)으로 가는데 계산된 최고의 가치이다.

