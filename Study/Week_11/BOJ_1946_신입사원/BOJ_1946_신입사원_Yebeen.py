# 둘 중 하나가 기준 값 보다 순위가 높아야 합격
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    rank = [[]for _ in range(N)]
    for i in range(N):
        rank[i]=list(map(int,input().split()))
    # 성적 기준으로 오름차순 정렬
    rank.sort(key=lambda x :x[0])
    cnt = 1
    base = rank[0][1] #기준을 맨 처음 면접성적을 잡음. 합격하려면 작아야함
    for i in range(1, N):
        if rank[i][1] < base:
            cnt += 1
            base = rank[i][1]
    print(cnt)
