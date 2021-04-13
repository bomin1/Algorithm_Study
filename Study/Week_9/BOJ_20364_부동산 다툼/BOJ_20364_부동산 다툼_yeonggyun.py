import sys
sys.stdin = open('input.txt')

N, Q = map(int, input().split())
ducks = [int(input())for _ in range(Q)]

# 방문 검사
visited = []

def go_duck(duck):
    # 와야하는길 탐색하기
    while duck > 1:
        duck //= 2
        # 누군가의 땅이라면 거기서 멈춰야 하므로 결과 정해짐
        if duck in visited:
            return duck
    visited.append(ducks[i])
    return 0


for i in range(Q):
    # 오리들 불러오기
    duck = ducks[i]
    print(go_duck(duck))




    
    







    