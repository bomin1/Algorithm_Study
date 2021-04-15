
N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

# 초기에는 무조건 첫 주유소에서 기름사서 가야함
total = distance[0] * price[0]
# 최솟값 설정
min_value = price[0]
# 실제 갈 거리 설정
d = 0

for i in range(1, N-1):
    # 싼 주유소를 찾았으면
    if price[i] < min_value:
        # 거리만큼 기름을 사자
        total += min_value * d
        # 싼곳의 가격
        min_value = price[i]
        # 거리 입력
        d = distance[i]
    else:
        # 싼곳이 아니라면 거리를 더해주자
        d += distance[i]

    # 마지막값은 제일 싼곳
    if i == N-2:
        total += min_value * d

print(total)

