import sys
sys.stdin = open("input.txt")

T = int(input())

def dfs(idx, check_score, check_calorie):
    global ans

    # 칼로리 넘어가면 끝
    if check_calorie > l:
        return
    # 마지막 인덱스에 도착했으면
    if idx == n:
        # 선호도가 높으면 갱신
        if check_score > ans:
            ans = check_score
        return

    # 재료 안사용
    dfs(idx +1 , check_score, check_calorie)
    # 재료 사용
    dfs(idx +1 , check_score+score[idx], check_calorie+calorie[idx])




for tc in range(1, T+1):

    # n : 재료의 수, l : 제한 칼로리
    n,l = map(int, input().split())
    score, calorie = [],[]
    for i in range(n):
        s,c = map(int, input().split())
        score.append(s)
        calorie.append(c)

    ans = 0
    dfs(0,0,0)
    
    print("#{} {}".format(tc, ans))

