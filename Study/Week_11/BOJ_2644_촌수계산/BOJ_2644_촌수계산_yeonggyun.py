import sys
sys.stdin = open("input.txt")

T = 1

# 두 사람의 촌수를 알아보기 위해 시작과 끝으로 나누어서 분석
def cal(start, end):
    # 방문했다는 것을 담기 위한 리스트 초기화
    visited = []
    # 현재 검사해야 하는 곳 초기화
    now = []
    # 촌수 초기화
    cnt = 0
    # 시작을 검사 리스트에 추가
    now.append(start)

    # 검사리스트에 존재할때까지 반복 - 가족관계가 있을때까지
    while now:
        # 있다면 일단 촌수 증가
        cnt += 1
        # 현재 검사해야하는 사람만큼 검사
        for _ in range(len(now)):
            # 현재 검사해야하는 사람을 추출
            temp = now.pop(0)
            # 만약 그사람이 목표한 사람이라면
            if temp == end:
                # 촌수에서 -1
                return cnt - 1
            # 해당 정보에 해당하는 가족관계를 검사
            for person in info[temp]:
                # 만약 그 사람이 검사한 사람이 아니라면
                if person not in visited:
                    # 검사 리스트에 추가
                    visited.append(person)
                    # 현재 검사할 리스트에 추가
                    now.append(person)
    # 만약 반복문이 끝났다면 관계가 없다는 것이므로 -1
    return -1


for tc in range(1, T+1):
    n = int(input())
    tar = list(map(int, input().split()))
    m = int(input())
    info = [[]for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        info[x].append(y)
        info[y].append(x)

    # 두대상을 계산하는 함수 사용
    print(cal(tar[0], tar[1]))









