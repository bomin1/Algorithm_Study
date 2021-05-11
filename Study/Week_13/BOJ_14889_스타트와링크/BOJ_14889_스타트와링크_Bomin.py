import sys
sys.stdin = open("input.txt")

T = int(input())

def solve(cnt, idx):
    global res
    if idx == n:
        return
    if cnt == n//2:
        start_score, link_score = 0,0
        for i in range(n-1):
            for j in range(i+1,n):
                if team[i] and team[j]:
                    start_score += arr[i][j]
                    start_score += arr[j][i]
                elif not team[i] and not team[j]:
                    link_score += arr[i][j]
                    link_score += arr[j][i]
        res = min(res,abs(start_score-link_score))
        print(team)
        return
    else:
        team[idx] = True
        solve(cnt+1,idx+1)
        team[idx] = False
        solve(cnt,idx+1)


for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    team = [False] * n
    res = 1e9
    solve(0,0)

    print("#{} {}".format(tc, res))

