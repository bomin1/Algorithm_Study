def DFS(num,cnt):
    global result,b
    if num == b:
        result = cnt
        return
    for i in range(len(tree[num])):
        if visited[tree[num][i]] == False:
            visited[tree[num][i]] = True
            DFS(tree[num][i], cnt+1)

n = int(input())
a, b = map(int, input().split()) # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(input()) #  부모 자식들 간의 관계의 개수
tree = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    x, y = map(int, input().split()) # 부모, 자식
    tree[x].append(y)
    tree[y].append(x)
# print(tree)
# print(visited)

result = -1

DFS(a,0)
print(result)
# print(visited)



