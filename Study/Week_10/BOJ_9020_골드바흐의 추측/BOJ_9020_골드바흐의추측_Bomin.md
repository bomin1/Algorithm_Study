# 9020_골드바흐의 추측



## 문제

1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.



## 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.



## 출력

각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

<br>

---

## Input

```txt
3
8
10
16
```

## Output

```
3 5
5 5
5 11
```

<br>

---

## Code

```python
import sys
sys.stdin = open("input.txt")
T=int(input())

def search_prime(n):
    check_prime = [i for i in range(n + 1)]
    # print('check_prime', check_prime)
    for i in range(2,int(n**0.5)+1):
        if check_prime[i] == 0:
            continue
        else:
            for j in range(i+i, n+1,i):
                check_prime[j] = 0
    print(check_prime)
    return check_prime

def solve(prime_nums):
    half_n = n//2

    for i in range(half_n,-1,-1):
        if not prime_nums[i]:
            continue
        for j in range(i,n):
            if not prime_nums[j]:
                continue
            if prime_nums[i] + prime_nums[j] == n:
                return i,j

for tc in range(1,T+1):
    n = int(input())
    prime_nums = search_prime(n)
    print(*solve(prime_nums))

```



## Review

**에라토스테네스의 체**

```python
def search_prime(n):
    check_prime = [i for i in range(n + 1)]
    for i in range(2,int(n**0.5)+1):
        if check_prime[i] == 0:
            continue
        else:
            for j in range(i+i, n+1,i):
                check_prime[j] = 0
    return check_prime
```

소수를 찾는 코드인데 우선 범위까지 `check_prime`이라는 리스트를 만들어서 소수는 그대로 남기고 소수가 아닌 숫자들은 0으로 만들어 줄 예정이다. 

이걸 볼 때 모든 숫자를 다 안보고 루트n까지만 봐도 충분하니까 범위를 `range(2,int(n**0.5)+1)`이렇게 잡아준다.

그렇게 하다보면 예를 들어 n=8이라고 하면 [0,1,2,3,0,5,0,7,0] 이런식으로 저장이 되어있을 것이다.

이게 에라토스테네스의 체로 소수를 판별하는 직관적이면서도 강력한 알고리즘이다.



1. 이제 소수를 찾았으면 소수의 차이가 가장 작으면서, 그 합이 n이 되는 두 수를 찾아야 하므로 리스트의 처음부터 접근하는게 아니라 가운데부터 접근하기 위해 half_n이라는 변수를 하나 만들어 줬고,
2. half_n을 기준으로 왼쪽으로 가면서 소수를 만나면 그 소수부터 오른쪽 끝까지 돌면서 더해서 n이 되는 숫자를 찾아본다.



