import sys
from itertools import permutations

input = sys.stdin.readline
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    balls = [list(map(int, input().split())) for _ in range(N)]

    # 0번 타자는 무조건 index 3번에
    # 그외 8명의 타자는 모든 경우의 수를 만들자

    hitter_index = list(range(1, 9))
    hitter = list(permutations(hitter_index))
    ans = 0
    for hit in hitter:
        hit = list(hit)
        hit.insert(3, 0)
        # print(hit)
        # [1, 5, 8, 0, 7, 4, 6, 3, 2]
        # 점수 저장용
        score = 0
        # 인덱스 움직일용
        index = 0
        # 이닝 시작
        for i in range(N):
            # 베이스 초기화
            base1, base2, base3 = 0, 0, 0
            # 아웃 카운트 초기화
            death_count = 0
            # 3아웃까지
            while death_count < 3:
                # 아웃 조건
                if balls[i][hit[index]] == 0:
                    death_count += 1
                # 1루타
                elif balls[i][hit[index]] == 1:
                    score += base3  # 1루타면 3루 득점
                    base1, base2, base3 = 1, base1, base2  # 한칸씩 밀기

                # 2루타
                elif balls[i][hit[index]] == 2:
                    score += (base2 + base3)  # 2루타면 2루,3루 득점
                    base1, base2, base3 = 0, 1, base1  # 두칸씩 밀기
                # 3루타
                elif balls[i][hit[index]] == 3:
                    score += (base1 + base2 + base3)  # 3루타면 1,2,3루 득점
                    base1, base2, base3 = 0, 0, 1  # 3칸 밀기
                else:
                    score += (base1 + base2 + base3 + 1)  # 홈런은 1,2,3루에 타자까지
                    base1, base2, base3 = 0, 0, 0  # 초기화
                # 그다음타자 인덱스
                index += 1
                if index == 9:
                    index = 0
        if score >= ans:
            ans = score
    print(ans)
