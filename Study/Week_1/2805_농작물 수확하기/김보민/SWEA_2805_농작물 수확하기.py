import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # arr = [list(map(int, list(input()))) for _ in range(n)]
    arr = [[int(val) for val in input()] for _ in range(N)]

    print(arr)

    res = 0
    for i in range(n):
        # J = 행에서 가운데 값
        j = n//2
        '''
        n = 5, j = 5//2=2
        1 - i=0                   (0,2)
        3 - i=1             (1,1),(1,2),(1,3)
        5 - i=2 => j     (2,0)(2,1)(2,2)(2,3)(2,4)
        3 - i=3              (3,1)(3,2)(3,2)   => 2(j)-1(i-j)칸만큼 양옆으로 칠하기 =
        1 - i=4                   (4,2)
        이런식으로 칠해질 떄 
        '''
        # 위 아래 값 1개
        if i == 0 or i == n-1:
            res += arr[i][j]
        else:
            if i <= j:
                for k in range(-i,i+1):
                    res += arr[i][j+k]
            else:
                for l in range(-(abs(j-(i-j))),abs(j-(i-j))+1,1):
                    res += arr[i][j+l]

    print("#{} {}".format(tc, res))

