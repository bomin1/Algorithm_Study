import sys
sys.stdin = open("input.txt")


n = int(input())

info = [list(input().split())for _ in range(n)]

# 결과들을 담을 리스트 초기화
results = []
# 로그를 분석
for i in range(n):
    # 만약 들어왔었다면 결과에 추가
    if info[i][1] == 'enter':
        results.append(info[i][0])
    # 나갔다면 결과에서 삭제
    if info[i][1] == 'leave':
        results.remove(info[i][0])
# 사전 역순으로 정렬
results.sort(reverse=True)
# 결과 출력
for result in results:
    print(result)










    


