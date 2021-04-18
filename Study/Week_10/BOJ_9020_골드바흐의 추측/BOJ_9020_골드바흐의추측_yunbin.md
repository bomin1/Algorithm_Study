# 9020 골드바흐의 추측

## 문제

1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

## 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

## 출력

각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

## 제한

- 4 ≤ n ≤ 10,000

## 예제 입력 1 

```
3
8
10
16
```

## 예제 출력 1

```
3 5
5 5
5 11
```

## 나의 코드

```python
import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

T = int(input())
for _ in range(1,T+1):

    N = int(input())
    result = [] 

    for i in range(1,N//2+1,2):

        min_num,max_num = i, N-i

        min_count = 0
        idx = 3 

        while idx <= min_num:

            if min_num %idx ==0:
                min_count +=1
            idx += 2
 
        max_count = 0
        idx = 3  

        while idx <= max_num:
            if max_num % idx ==0:
                max_count +=1
            idx += 2


        if min_count ==1 and max_count ==1:
            result= [min_num,max_num]


    print(*result)
```

처음 풀이, 답은 나오지만, 시간 초과에 또 빠져버렸다...

아래 코드가 정답코드다 

```python
import sys
import math
input = sys.stdin.readline
# sys.stdin = open('input.txt')

T = int(input())


def is_prime_number(x):
    for j in range(2, int(math.sqrt(x)) + 1):
        if x % j == 0:
            return False
    return True


for tc in range(1, T + 1):
    N = int(input())
    result = []
    for i in range(N // 2, 1, -1):

        if is_prime_number(i) and is_prime_number(N - i):
            result.append([i,N-i, (N-i-i)])

    result.sort(key= lambda x:x[2])
    print(result[0][0],result[0][1])
```

## 풀이

처음엔 아무생각없이 일단 풀었는데, 시간초과의 늪에 빠졌다. 소수를 처리할때 나오는 while문들이 많아서 짝수번호는 빼보고, 가장 작은 차이를 가져오기 위해 중간에서부터 소수를 찾는다던가 여러가지를 해봤는데, 계속계속계속 시간초과가 떴다. 

O(n)에다가 숫자 나올때마다 계속 연산을 해줘야되니까 소수를 찾는 다른 방법을 찾아야 했다. 

[소수판별알고리즘](https://velog.io/@koyo/python-is-prime-number 에서 조금 더 효율적인 알고리즘을 찾았는데, x의 제곱근까지만 확인하면 소수 판별이 가능하다는 것이였다,

예를 들자면 16의 약수는 [1,2,4,8,16] 인데 해당 수의 가운데 수를 기준으로 대칭적으로 곱을 통해 16을 만들 수 잇으므로 절반만 보면 된다! 

그렇게 문제를 제출 하니까 이제는 **틀렸습니다!**가 떴고.... 아무래도 처음에는 중간에서 시작해서 소수를 찾으면 break 문을 걸어 끝내는 식으로 했는데, 

해결방법은 무식하지만 두 수의 차이를 포함한 모든 소수들을 저장해서 두수의 차이를 기준으로 정렬시켜버렸다. 

그 다음에 가장 작은 값인 인덱스 0인 두 소수들을 가져왔다! 







