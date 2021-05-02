import sys
sys.stdin = open("input.txt")
from collections import deque

T=1

def cal():
    q = deque()
    # 내가 찾아야 할 위치를 제일 처음 큐에 넣어준 다음
    q.append(a)
    # 큐를 돌면서
    while q:
        # 해당 위치를 계속 갱신한다.
        now = q.popleft()
        # 지금 위치가 내가 찾아야할 또 다른 위치와 같다면 끝
        if now == b:
            break

        # 같지않다면 지금 노드의 자식노드에 접근을 해서 
        for i in check[now]:
            # 그 자식노드가 방문처리가 되지 않았다면 우선 큐에 넣어준 다음, 방문처리 해주고 해당 위치의 거리는 부모노드의 값에 +1을 한 값을 넣어 갱신해준다. 
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                distance[i] = distance[now] + 1
                

    # 친척관계가 전혀 없다는 말은 이어지지 않았고 이 말은 해당노드의 거리가 0임을 의미한다.
    if distance[b] == 0:
        return -1
    else:
        return distance[b]

# 전체 사람 수
n = int(input())
# 촌수를 계산해야하는 사람의 번호
a,b = map(int, input().split())
# 몇개 있는지
m = int(input())

# 거리 저장 리스트
distance = [0 for _ in range(n+1)]

# 방문체크
visited = [0 for _ in range(n+1)]

# 부모 자식 저상하는 인접 리스트
check = [[] for _ in range(n+1)]

# 부모 자식 관계, 양방향으로 받아옴
for i in range(m):    
    parent, child = map(int, input().split())
    check[parent].append(child)
    check[child].append(parent)

print(cal())