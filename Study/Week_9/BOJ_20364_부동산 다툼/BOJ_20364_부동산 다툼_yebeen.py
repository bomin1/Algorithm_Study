# N :땅 개수, Q:오리 수
N, Q = map(int, input().split())
tree = [0 for _ in range(N+1)] #인덱스 N까지 나타내주기 위해서 N+1까지 만들어줌 맨 첫 0 인덱스는 안씀
for dock in range(1, Q+1): #i:트리 인덱스(땅번호)
    ground = int(input())
    cnt = 0
    while ground > -1:
        ground /= 2
        cnt += 1
        if int(ground) == 1:
            tree[int(ground*2*cnt)] = dock
            print(0)
            break
        # if tree[int(ground)] == 0:
        #     continue
        if tree[int(ground)] != 0:
            print(int(ground))
            break
# print(tree)
###내가 푼방법 : 부모노드에 0이 아닌것이 존재한다면 부모노드를 출력하고, 부모부터 루트노드까지
#모두 다 0 이면 해당 노드에 값을 넣어주고 0을 출력한다.
##시간초과다ㅜㅜㅜㅜ