import sys
sys.stdin = open("input.txt")

n,m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
test_arr = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]

res = [[0 for _ in range(m)] for _ in range(n)]
sum_val = 0

for i in range(m):
    sum_val += arr[0][i]
    res[0][i] = sum_val

for i in range(1,n):
    # 위에서 아래로
    for j in range(m):
        test_arr[i][j][0] = res[i-1][j] + arr[i][j]
        test_arr[i][j][1] = res[i-1][j] + arr[i][j]

    # 왼쪽에서 오른쪽으로 [ 0]번째
    for j in range(1,m):

        test_arr[i][j][0] = max(test_arr[i][j][0], test_arr[i][j-1][0] + arr[i][j])

    # 오른쪽에서 왼쪽으로 [ 1]번째
    for j in range(m-2,-1,-1):
        test_arr[i][j][1] = max(test_arr[i][j][1], test_arr[i][j+1][1] + arr[i][j])

    for j in range(m):
        res[i][j] = max(test_arr[i][j][0], test_arr[i][j][1])

print(res[-1][-1])

