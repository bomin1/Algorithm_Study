import sys
from collections import deque
sys.stdin = open('input.txt')
# input = sys.stdin.readline

T = int(input())

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    cnt = 0 
    while queue:
        x = queue.popleft()
        for node in graph[x]:
            if not visited[node]:
                visited[node] =True
                cnt +=1
                queue.append(node)

    return cnt 
for tc in range(1,T+1):
    N, M = map(int,input().split())

    visited = [False for _ in range(N+1)]

    graph = [[] for _ in range(N+1)]


    for _ in range(M):
        node, child = map(int,input().split())
        graph[node].append(child)
        graph[child].append(node)
    # print(graph)
    # [[], [2, 3], [1, 3], [2, 1]]

    ans = 0 

    ans = bfs(1)

    print(ans)