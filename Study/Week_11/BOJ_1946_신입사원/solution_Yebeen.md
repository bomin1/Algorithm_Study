# 1946. 신입사원

## 풀이

문제를 해석해보면 등수가 두가지가 있는데 공동 등수는 없다고 했으므로

하나의 등수를 기준으로 오름차순 정렬을 해놓고 맨 앞의 것을 기준으로 잡는다.

나는 서류심사 성적을 기준으로 잡았고, 면접 성적을 비교하는 방법으로 했다.

![img](https://blog.kakaocdn.net/dn/kNNoz/btq3mirk0iP/rHk4fvatwmggFVBv3mrhM1/img.png)

기준이 되는 (사각형) 면접 성적보다 숫자가 낮아야 등수가 높다는 뜻이므로 리스트를 순차적으로 반복하면서 작은 수가 나올 때까지 기준을 바꾸지 않는다.

작은 수가 나오면 카운트를 해주고 기준을 갱신해준다.

마지막으로 카운트 개수를 출력하면 됨

## 코드



```python
# 둘 중 하나가 기준 값 보다 순위가 높아야 합격
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    rank = [[]for _ in range(N)]
    for i in range(N):
        rank[i]=list(map(int,input().split()))
    # 성적 기준으로 오름차순 정렬
    rank.sort(key=lambda x :x[0])
    cnt = 1
    base = rank[0][1] #기준을 맨 처음 면접성적을 잡음. 합격하려면 작아야함
    for i in range(1, N):
        if rank[i][1] < base:
            cnt += 1
            base = rank[i][1]
    print(cnt)
```