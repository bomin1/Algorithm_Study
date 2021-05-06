# 회사에 있는 사람 

## 문제

상근이는 세계적인 소프트웨어 회사 기글에서 일한다. 이 회사의 가장 큰 특징은 자유로운 출퇴근 시간이다. 따라서, 직원들은 반드시 9시부터 6시까지 회사에 있지 않아도 된다.

각 직원은 자기가 원할 때 출근할 수 있고, 아무때나 퇴근할 수 있다.

상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 로그에 기록된 출입 기록의 수 n이 주어진다. (2 ≤ n ≤ 106) 다음 n개의 줄에는 출입 기록이 순서대로 주어지며, 각 사람의 이름이 주어지고 "enter"나 "leave"가 주어진다. "enter"인 경우는 출근, "leave"인 경우는 퇴근이다.

회사에는 동명이인이 없으며, 대소문자가 다른 경우에는 다른 이름이다. 사람들의 이름은 알파벳 대소문자로 구성된 5글자 이하의 문자열이다.

## 출력

현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.

## 예제 입력 1 

```
4
Baha enter
Askar enter
Baha leave
Artem enter
```

## 예제 출력 1 

```
Askar
Artem
```



## 풀면서 느낀점

예전에 다른 문제를 풀면서 for문을 입력받을때마다 if ~in 연산자를 사용하면 시간복잡도가 O(N)이라서 문제가 안풀렸던 기억이 나서 이문제는 그렇게 상관이 없는 것 같지만, 중복이 없는 이름을 주어지기에 연산이 더빠른 set을 사용했다.

enter를 받으면 명단에 넣고, 그게 아니라면 퇴근시켜주고 출력을 사전순의 역순으로 하라고 해서 list로 만들어 정렬 해줬다.



## 나의 코드

```python
N = int(input())

result = set()
for i in range(N):
    name, status = map(str, input().split())

    if status == 'enter':
        if name not in result:
            result.add(name)
    else:
        if name in result:
            result.remove(name)

result = list(result)
result.sort(reverse=True)
# for i in range(len(result)):
#     print(result[i])
print(*result , sep='\n')
```

