N = int(input()) # 도시의 개수
dis = list(map(int,input().split()))
money = list(map(int,input().split()))

result = 0

for i in range(0, len(money)-1): # 마지막 money값은 사용 안함
    if i == 0: # 먼저 첫 번째 money를 최소값으로 세팅
        min_m = money[0]
        result += min_m * dis[i] # 결과값에 더해주고 다음 반복문으로 넘어감
        continue
    elif min_m > money[i]: # 최소값이 다음 money값 보다 크면
        min_m = money[i] # 최소값 업데이트
        result += min_m * dis[i] # 결과값에 더해주고 다음 반복문으로 넘어감
        continue
    else: # 결과값에 더해준다.
        result += min_m * dis[i]
print(result)