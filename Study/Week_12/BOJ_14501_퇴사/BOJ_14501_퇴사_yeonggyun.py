import sys
sys.stdin = open("input.txt")

T = 4


for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split()))for _ in range(N)]

    # 총합을 나타낼 리스트
    totals = [0] * N
    # N만큼 돌면서 검사
    for i in range(N):
        # 만약 현재 날짜와 끝나는 날짜를 했을때 기간내에 끝낼 수 있다면
        if i + info[i][0] <= N:
            # 현재 날짜에 벌수 있는 돈을 기록
            totals[i] = info[i][1]
            # 현재까지 날짜를 되돌아 보면서 추가
            for j in range(i):
                # 현재 날짜 내에 수행할 수 있다면
                if j + info[j][0] <= i:
                    # 기존의 수행값과 새로운 값중 가장 큰 값을 기록
                    totals[i] = max(totals[i], totals[j] + info[i][1])
    # 총 토탈리스트 중에서 가장 큰 돈을 벌수 있는 값 출력
    print(max(totals))



