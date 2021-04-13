import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    info = [list(map(int, input().split()))for _ in range(M)]
    # 항상 연결 그래프를 그리고 있으므로 그냥 N-1개이다.....
    print(N-1)