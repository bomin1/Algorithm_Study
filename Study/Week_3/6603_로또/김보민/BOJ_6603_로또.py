import sys
sys.stdin = open("input.txt")

def dfs(start):
    if len(res) == 6:
        print(*res)
        return

    for i in range(start, k):
        if not visited[i]:
            visited[i] = True
            res.append(s[i])
            dfs(i+1)

            res.pop()
            visited[i]=False

while True:
    k, *s = list(map(int, input().split()))

    if k == 0:
        break

    res = []
    visited = [False]*k
    dfs(0)
    print()

