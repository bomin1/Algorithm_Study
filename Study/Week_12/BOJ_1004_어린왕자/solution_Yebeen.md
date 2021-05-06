# 풀이

문제를 보니까 시작점 또는 끝점이 원 안에 있으면 카운트를 높여주면 되는 문제 같았다.

 원의 방정식을 생각해보면

(<u>x</u>-x좌표)^2 + (<u>y</u>-y좌표)^2 = 반지름길이^2 (x좌표 , y좌표 :원의 중심)인데,

이 식에 <u>x</u>와 <u>y</u>에 점을 넣어서 반지름^2보다 작으면 그 점은 원 안에 있는 것이다.

ex) x^2+y^2 =2^2인 원의 방정식이 있을 때 (1,1)이 원 안에 존재하는지 여부는 식에 넣으면 된다.

1+1 < 4이기 때문에 점(1,1)은 원 안에 있다.



```python
##런타임에러(EOFError)
T = int(input()) # 테케
# 행성계 진입/이탈 횟수를 최소화
for tc in range(T+1):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input()) # 행성계의 개수
    cnt = 0
    for i in range(n):
        cx, cy, r = map(int, input().split()) # 행성계의 중점과 반지름
        # 행성 원 안에 시작점 or 도착점이 존재한다면 cnt += 1
        if (x1-cx)**2 + (y1-cy)**2 < r**2: # 시작점이 원안에 존재
            cnt += 1
        if (x2-cx)**2 + (y2-cy)**2 < r**2: # 끝점이 원안에 존재
            cnt += 1

    print(cnt)
```

input()을 sys.stdin.readline()방법으로 고쳐봤는데도 이번엔 valueError로 바뀌었다..

```python
##50%까지 가다가 런타임에러(ValueError)
import sys,math
T = int(sys.stdin.readline().strip()) # 테케
# 행성계 진입/이탈 횟수를 최소화
for tc in range(T+1):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline().strip()) # 행성계의 개수
    cnt = 0
    for i in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split()) # 행성계의 중점과 반지름
        # 행성 원 안에 시작점 or 도착점이 존재한다면 cnt += 1
        if math.pow((x1-cx),2) + math.pow((y1-cy),2) < math.pow(r,2): # 시작점이 원안에 존재
            cnt += 1
        if math.pow((x2-cx),2) + math.pow((y2-cy),2) < math.pow(r,2): # 끝점이 원안에 존재
            cnt += 1

    print(cnt)
```

이러다가 경우가 하나 더 생각 났다.

시작점과 끝점이 한 원 안에 있을 때!

```python
##50%까지 가다가 런타임에러(ValueError)
import math
import sys
input = sys.stdin.readline

T = int(input()) # 테케
# 행성계 진입/이탈 횟수를 최소화
for tc in range(T+1):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input()) # 행성계의 개수
    cnt = 0
    for i in range(n):
        temp = 0
        cx, cy, r = map(int, input().split()) # 행성계의 중점과 반지름
        # 행성 원 안에 시작점 or 도착점이 존재한다면 cnt += 1
        if (x1-cx)**2 + (y1-cy)**2 < r**2: # 시작점이 원안에 존재
            cnt += 1
            temp += 1
        if (x2-cx)**2+ (y2-cy)**2 < r**2: # 끝점이 원안에 존재
            cnt += 1
            temp += 1
        if temp == 2: # 시작점과 끝점이 같은 원 안에 있을 때는 temp == 2
            cnt -= 2 # 위에서 cnt 2를 더해줬으니까 뺀다

    print(cnt)
```

그래도 에러나네