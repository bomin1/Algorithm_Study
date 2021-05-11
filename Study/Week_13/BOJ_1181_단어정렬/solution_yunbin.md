# 단어 문제

알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로

## 입력

첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

## 출력

조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

## 예제 입력 1 복사

```
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
```

## 예제 출력 1 복사

```
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
```



## 풀면서 느낀점

일단 길이 순으로 정렬해야하기때문에 주어지는 최대길이인 50를 만들어놓고 단어를 우선 정렬하려고 했다. 

그다음 그 안에서 중복도 없애고, 사전순으로 만들어야되서, 먼저 중복을 없애기 위해 result를 set으로 만들어서 중복을 없애고 

중복을 없앤 result를 다시 리스트로 바꿔서 솔팅해준다음 출력해주는 방법으로 문제를 해결했다. 



```python
import sys

sys.stdin = open('input.txt')

N = int(input())

arr = [[] for _ in range(51)]
for i in range(N):
    a = input()
    arr[len(a)].append(a)


for i in range(51):
    result = set()
    if arr[i]:
        for j in arr[i]:
            result.add(j)

        result =list(result)
        result.sort()
        print(*result ,sep='\n')