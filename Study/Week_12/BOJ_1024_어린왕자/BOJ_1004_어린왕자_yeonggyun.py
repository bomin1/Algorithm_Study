import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    info = [list(map(int, input().split()))for _ in range(n)]
    # 횟수 초기화
    cnt = 0
    # n만큼 반복
    for i in range(n):
        # 시작점검사
        # 시작점과 원과의 거리
        d1 = ((x1 - info[i][0]) ** 2 + (y1 - info[i][1]) ** 2) ** 0.5
        # 도착점과 원과의 거리
        d2 = ((x2 - info[i][0]) ** 2 + (y2 - info[i][1]) ** 2) ** 0.5
        # 만약 시작점과 도착점이 모두 한원안에 있다면 이탈, 진입 x
        if d1 < info[i][2] and d2 < info[i][2]:
            continue
        # 한쪽이 그렇다면 필요함
        if d1 < info[i][2] or d2 < info[i][2]:
            cnt += 1
    print(cnt)