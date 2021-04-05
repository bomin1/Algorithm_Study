import sys

sys.stdin = open("input.txt")

T = int(input())

def dfs(v,cnt):
    global ans
    visited[v] = 1
    if cnt > ans:
        ans = cnt

    for i in range(1,n+1):
        if arr[v][i] and not visited[i]:
            dfs(i, cnt+1)
    visited[v] = 0


for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    # print(arr)
    visited = [False] * (n + 1)
    print(visited)
    ans = 0


    for i in range(m):
        x,y = map(int, input().split())
        arr[x][y], arr[y][x] = 1, 1

    print(arr)

    for i in range(1,n+1):
        dfs(i,1)
    print(ans)
