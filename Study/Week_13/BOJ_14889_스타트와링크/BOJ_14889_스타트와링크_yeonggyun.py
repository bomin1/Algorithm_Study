

# dfs 활용
# 팀을 하나씩 만들어가면서 각각의 값을 체크하는 과정이었다.

# 먼저 검사하는 idx와 팀을 정확히 반으로 나누기 위해 인원수를 세줄 cnt 초기화
def dfs(idx, cnt):
    global result
    # 문제에서 N은 짝수라고 주어짐
    # 만약 절반을 편을 뽑았다면 검사해보자
    if cnt == N/2:
        # start 팀과 link팀 각각 초기화
        start, link = 0, 0
        # arr을 검사하기 위한 이중 for문
        for i in range(N):
            for j in range(N):
                # 만약 방문기록이 있다면, 즉 팀에 뽑힌 흔적이 있다면
                if visited[i] and visited[j]:
                    # 스타트 팀에 데려갈 것이다.
                    start += arr[i][j]
                # 팀에 뽑힌 흔적이 없다면 자동으로 link팀에 합류
                elif not visited[i] and not visited[j]:
                    # 링크팀 역시 능력치 더해준다.
                    link += arr[i][j]
        # 이를 통해 얻어진 팀원능력치 차이와 기존의 result와 비교하여 결과값 갱신
        result = min(result, abs(start-link))

    # 팀원을 뽑는 과정
    for i in range(idx, N):
        # 만약 뽑지 않은 사람이라면
        if not visited[i]:
            # 뽑았다고 체크
            visited[i] = 1
            # 다음 사람 뽑자
            dfs(i+1, cnt+1)
            # 뽑았던 사람 취소하기(백트래킹 위함)
            visited[i] = 0


N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
# 뽑았는지 방문기록
visited = [0 for _ in range(N)]
# 능력치가 100씩 총 20명이 최대이므로 한팀엔 10명이 최대일 것이다.
result = 100*10

# 인덱스 0부터 0명으로 시작
dfs(0, 0)
print(result)


