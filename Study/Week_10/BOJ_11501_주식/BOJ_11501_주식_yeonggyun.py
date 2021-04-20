import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    # 기본원리
    # 뒤에서 부터 계산하며 맥스를 갱신해간다.
    # 맥스가 아닐경우는 이득이 되는 경우 이므로 현재 맥스값과 차이를 결과에 반영

    # 결과값 초기화
    result = 0
    # 뒤에서 부터 검사할것 이기 때문에 맨 뒤에 값을 맥스값 초기화
    max_value = price[-1]
    # 맨뒤부터 돌기
    for i in range(N-1, -1, -1):
        # 맥스값보다 크거나 같다면 -> 아무것도 안함 그냥 갱신
        if price[i] >= max_value:
            max_value = price[i]
        else:
            # 작다면 그것은 이득임
            result += max_value - price[i]

    print(result)



