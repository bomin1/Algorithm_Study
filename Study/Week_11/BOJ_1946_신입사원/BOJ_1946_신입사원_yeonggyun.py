import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split()))for _ in range(N)]
    # 서류 점수를 1등부터 세우기 위해서 정렬함
    info.sort()
    # intervies score -> is
    # 인터뷰 점수를 서류점수가 높은순으로 시작
    # 등수가 낮은 순 으로 시작
    low_is = info[0][1]
    # 서류점수 1등은 무조건 뽑힐 것 이기 때문에 1부터 시작
    cnt = 1
    for i in range(N):
        # 만약 서류에서 상위 랭크를 차지하고 있는 사람보다 인터뷰 등수가 낮다면
        # 점수가 높은것 이므로
        if low_is > info[i][1]:
            # 한명 더 뽑을 수 있다.
            cnt += 1
            # 다음그사람 점수로 적용
            low_is = info[i][1]
    # 몇명 뽑는지 출력
    print(cnt)






