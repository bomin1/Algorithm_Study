[toc]



# BOJ 9020 골드바흐의 추측

## 문제

1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

### 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

### 출력

각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

### 제한

- 4 ≤ n ≤ 10,000





## 풀이과정



```python
T = int(input())

def check(number):
    for i in range(2, number//2 + 1):
        if not number % i:
            return False
    return True

for tc in range(1, T+1):
    n = int(input())

    L = int(n/2)
    R = int(n/2)
    idx = 0
    while L > 0 and R < n:
        L -= idx
        R += idx

        if check(L) and check(R):
            break
        else:
            idx += 1

    print(L, end=' ')
    print(R)
```

* 위와같이 풀었는데 사정없이 틀려버렸다.
  * print형식도 고쳐가며 해봤는데 역시 틀렸다.



## 풀이

```python
import sys
sys.stdin = open("input.txt")

T = int(input())

# 소수인지 체크하는 함수
def check(number):
    # 제곱근을 기준으로 두수의 곱으로 약수를 나타낼 수 잇따.
    for i in range(2, int(number**0.5)+1):
        # 만약 나머지가 없는 값이 존재한다면 약수가 존재한다는 것
        if not number % i:
            # 따라서 소수가 아님
            return False
    # 검사를 통과했다면 소수임
    return True


for tc in range(1, T+1):
    n = int(input())

    # 왼쪽 오른쪽수를 각각 반으로 나눠줌
    L = int(n/2)
    R = int(n/2)

    result = []

    while True:
        # 만약 둘다 소수라면 결과에 더해준다.
        if check(L) and check(R):
            result.append((L, R, R-L))

        L -= 1
        R += 1

        #  다 검사했으면 종료
        if L < 1:
            break
    # 차이값을 기준으로 정렬한다.
    result.sort(key=lambda x: x[2])
    # 가장 차이가 적은 값이 맨 앞에 오므로 이를 출력
    print(result[0][0], result[0][1])

```



## 추가

* 왜인지 모르겠지만 break를 통해서 나온 값은 인정이 안되고 다뽑아서 적은 순으로 정렬한 값은 정답이 됐다.
* 왜지... 왜인거야..😭