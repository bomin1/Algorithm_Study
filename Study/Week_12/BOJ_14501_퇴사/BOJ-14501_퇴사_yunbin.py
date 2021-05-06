
# sys.stdin = open('input.txt')

N = int(input())


def dfs(idx,mysum):
    global result
    # print(idx,mysum)
    if idx <= N+1 and mysum >= result:
        result =mysum
        # print(idx,result)
    if idx >N:
        return


    dfs(idx+arr[idx][0], mysum+ arr[idx][1])

    dfs(idx+1, mysum)
visited = [False for _ in range(N+1)]

arr = [list(map(int,input().split())) for _ in range(N)]
arr.insert(0,[0,0])
# [[0, 0], [3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]
result= 0
dfs(1,0)
print(result)



