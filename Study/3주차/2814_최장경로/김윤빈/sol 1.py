import sys

sys.stdin = open('sample_input.txt')
T = int(input())



def DFS(node, count):
    # local variable 'result' referenced before assignment 처리
    global result
    # 도장찍고
    visited[node] = True
    # print(visited)
    # count 세고
    count += 1
    # 재귀로 count되는 max값만 저장
    if result < count:
        result = count
    # 연결된 노드중 방문 안했으면 DFS 다시 실행해서 count를 늘림
    for v in edge_list[node]:
        if not visited[v]:
            DFS(v, count)
    # 다음 for문을 위해 초기화
    visited[node] = False

    print(visited)
for tc in range(1, T + 1):
    # DFS 실행,
    # 모든 노드를 시작점으로 DFS 실행 후 가장 긴 count 찾기

    # 그래프 생성
    # N: 노드 수 , M : 간선수
    N, M = map(int, input().split())

    edge_list = [[] for _ in range(N + 1)]
    for _ in range(M):
        start_node, end_node = map(int, input().split())
        # 무지향성
        edge_list[start_node].append(end_node)
        edge_list[end_node].append(start_node)

    # print(edge_list)
    # [[], [2], [1, 3], [2]]
    result = 0
    result = 0
    visited = [False] * (N + 1)
    for node in range(N + 1):
        DFS(node, result)

    print("#{} {}".format(tc, result))
