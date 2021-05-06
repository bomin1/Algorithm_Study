import sys
sys.stdin = open("input.txt")

def DFS(day,pay):
    global res
    if day == N: #일 수가 N보다 커지면
        if res < pay: #원래있는 페이의 합 보다 크면 갱신
            res = pay
        return
    elif day > N:
        return

    DFS(day+1,pay) #선택 안하는 경우
    if day + L[day][0] <= N: #선택 하는 경우
        DFS(day+L[day][0],pay+L[day][1])


N = int(input()) # N+1되는 날에 퇴사함
# T = []
# P = []
L =[]
for i in range(N):
    t, p = map(int, input().split())
    # T.append(t)
    # P.append(p)
    L.append([t,p])
res = 0
DFS(0,0)
print(res)

