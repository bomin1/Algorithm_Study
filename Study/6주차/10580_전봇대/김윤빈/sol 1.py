import sys

sys.stdin = open('input.txt')

T = int(input())
result = 0
for tc in range(1, T + 1):
    N = int(input())

    tower = [list(map(int,input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(i+1,N):

            if tower[i][0] < tower[j][0]:
                if tower[i][1] > tower[j][1]:
                    result += 1

            else:
                if tower[i][1] < tower[j][1]:
                    result += 1

    print("#{} {}".format(tc,result))


