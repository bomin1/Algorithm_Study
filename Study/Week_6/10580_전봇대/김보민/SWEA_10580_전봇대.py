import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # 교차점의 갯수
    cnt = 0

    lst = []

    for i in range(n):
        a,b = map(int, input().split())

        if lst:
            for check in lst:
                if (a-check[0]) * (b-check[1]) < 0:
                    cnt += 1
            lst.append((a,b))
        else:
            lst.append((a,b))

        '''
        i = 0. lst = [(1,10)]
        i = 1. a,b = 5,5 / check=(1,10) / lst = [(1,10),(5,5)]
        i = 2. a,b = 7,7 / check=(1,10) /
                         / check=(5,5)  / lst = [(1,10),(5,5),(7,7)]
        
        '''

    print('#{} {}'.format(tc, cnt))




    # line = [list(map(int,input().split())) for i in range(n)]



    
    # print("#{} ".format(tc, ))

