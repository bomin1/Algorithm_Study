import sys
sys.stdin = open("input.txt")
from itertools import permutations
import pprint
T=int(input())

for tc in range(1,T+1):
    n = int(input())
    innings = [list(map(int, input().split())) for _ in range(n)]
    # 4 0 0 0 0 0 0 0 0
    # 4 0 0 0 0 0 0 0 0

    player = [2,3,4,5,6,7,8,9]
    ans = 0

    for order in permutations(player,8):
        # 4번 주자 추가하기
        # order.insert(3,1)
        # print(order)
        # 아니 순열 튜플로 들어오네;;;
        order = list(order)
        order.insert(3, 1)
        # print(order)
        # [7, 4, 5, 1, 3, 6, 2, 9, 8]
        # [7, 4, 5, 1, 3, 6, 8, 2, 9] - order

        score = 0
        hitter_order = 0

        '''
        안타: 1
        2루타: 2
        3루타: 3
        홈런: 4
        아웃: 0
        '''
        # 4 0 0 0 0 0 0 0 0
        for inning in innings:
            out = 0
            runner1,runner2,runner3 = 0,0,0
            while out < 3:
                # 이닝[주자번호]
                # 주자 번호 : order로 접근

                # 아웃인 상황
                if inning[order[hitter_order]-1] == 0:
                    out += 1
                elif inning[order[hitter_order]-1] == 1:
                    score += runner3
                    runner1, runner2, runner3 = 1, runner1, runner2
                elif inning[order[hitter_order]-1] == 2:
                    score += (runner2+runner3)
                    runner1, runner2, runner3 = 0, 1, runner1
                elif inning[order[hitter_order]-1] == 3:
                    score += (runner1 + runner2 + runner3)
                    runner1, runner2, runner3 = 0, 0, 1
                elif inning[order[hitter_order]-1] == 4:
                    score += (runner1 + runner2 + runner3+1)
                    runner1, runner2, runner3 = 0, 0, 0

                hitter_order += 1
                if hitter_order == 9:
                    hitter_order = 0

        ans = max(ans,score)
    print(ans)







