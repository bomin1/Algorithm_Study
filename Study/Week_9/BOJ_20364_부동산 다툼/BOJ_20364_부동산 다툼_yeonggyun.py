import sys
sys.stdin = open('input.txt')

N, Q = map(int, input().split())
ducks = [int(input())for _ in range(Q)]

# 방문 검사
visited = set()

for i in range(Q):
    result = 0
    # 오리들 불러오기
    duck = ducks[i]
    # 와야하는길 탐색하기
    while duck > 1:
        # 누군가의 땅이라면 거기서 멈춰야함
        # 하지만 거꾸로 거슬러 올라가기 때문에 가장 높은 조상을 계속 갱신
        if duck in visited:
            result = duck
        duck //= 2
    visited.add(ducks[i])
    print(result)