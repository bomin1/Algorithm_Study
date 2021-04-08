# 백준 1764.듣보잡

# 듣보잡 성공분류

![img](chrome-extension://anenheoccfogllpbpcmbbpcbjpogeehe/svg/7.svg) Silver IV
[자료 구조](https://solved.ac/problems/tags/data_structures)[정렬](https://solved.ac/problems/tags/sorting)[문자열](https://solved.ac/problems/tags/string)
난이도 제공: solved.ac — [난이도 투표하러 가기](https://solved.ac/contribute/1764)

| 시간 제한 | 메모리 제한 | 제출  | 정답  | 맞은 사람 | 정답 비율 |
| :-------- | :---------- | :---- | :---- | :-------- | :-------- |
| 2 초      | 256 MB      | 26169 | 10632 | 7655      | 39.704%   |

## 문제

김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 영어 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

 

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

## 출력

듣보잡의 수와 그 명단을 사전순으로 출력한다.

## 예제 입력 1 

```
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
```

## 예제 출력 1 

```
2
baesangwook
ohhenri
```

## 나의 코드

```python
N, M =map(int,input().split())
no_hear = []
no_see = []
no_list = []
for i in range(N):
    a = input()
    no_hear.append(a)
for i in range(M):
    b = input()
    no_see.append(b)
    ####  in으로 했더니 시간초과!!!!!!!!!!!!!
    # if b in no_hear:
    #     no_list.append(b)
#리스트를 집합으로 만들어주고 교집합을 구한뒤 다시 리스트로 바꾼다.
no_list = list(set(no_hear) & set(no_see))
#사전순
no_list.sort()

print(len(no_list))
for i in range(len(no_list)):
    print(no_list[i])
```

## 풀이

1. 듣지 못한 명단을 리스트로 받고

2. 보지 못한 명단도 리스트로 받는다

3. 두가지 리스트를 set으로 집합으로 만들어준다음 교집합을(&) 구한 뒤에 다시 list로 만들어준다.

4. 듣도보도 못한 리스트를 사전순으로 sort해주고 출력

 

처음에 그냥 리스트 in을 사용해서 처리해줬는데 시간초과가 떴다. 리스트를 다 보아야해서 시간이 오래걸리는 것 같다. :(