import sys
from collections import deque

# sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())

start, end = map(int, input().split())

M = int(input())

edge_list = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for i in range(M):
    parent, child = map(int, input().split())
    edge_list[parent].append(child)
    edge_list[child].append(parent)

# print(edge_list)
# [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]

visited[start] = True
queue = deque()
queue.append([start, 0])

while queue:
    now, count = queue.popleft()

    if now == end:
        print(count)
        break
    count += 1
    for i in edge_list[now]:
        if not visited[i]:
            visited[i] = True
            queue.append([i, count])
else:
    print(-1)
