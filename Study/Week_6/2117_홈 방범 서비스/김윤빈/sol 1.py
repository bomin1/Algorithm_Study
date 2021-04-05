import sys

sys.stdin = open('sample_input.txt')
T = int(input())
'''
수업내용참고 > 좌표당 k값에따른 집갯수 구해서 넣기 

운영 비용 = K * K + (K - 1) * (K - 1)

운영 영역의 크기 K 는 1 이상의 정수이다.

 - K = 1 일 때, 운영 비용은 1 이다.

 - K = 2 일 때, 운영 비용은 5 이다.

 - K = 3 일 때, 운영 비용은 13 이다.

 - K = 4 일 때, 운영 비용은 25 이다.

'''
for tc in range(1, T + 1):
    # 도시의 크기 N과 하나의 집이 지불할 수 있는 비용 M
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    # 집의 위치 찾기
    houses = []
    for i in range(N):
        for j in range(N):
            if city[i][j]:
                houses.append([i, j])
    # print(house) # [[0, 5], [1, 1], [1, 3], [1, 7], [3, 3], [3, 5], [4, 2], [4, 3], [6, 4], [6, 6], [7, 0]]
    # k가 1일땐 한집밖에 없다.
    result = 1
    # 완전탐색

    for k in range(2, 2*N):
        for i in range(N):
            for j in range(N):
                count = 0
                # 다이아몬드 형태 좌표값안으로 들어오는지 체크
                for house in houses:
                    if abs(i - house[0]) + abs(j - house[1]) < k:
                        count += 1
                # 가장많은집 + 손해안날때 count 갱신
                if count > result and count * M >= k * k + (k - 1) * (k - 1):
                    result = count
    print("#{} {}".format(tc, result))
