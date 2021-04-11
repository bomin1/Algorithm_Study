N, M =map(int,input().split())
no_hear = []
no_see = []
no_list = []
for i in range(N):
    a = input()
    no_hear.append(a)
for i in range(M):
    b = input()
    no_see.append(b)
    ####  in으로 했더니 시간초과!!!!!!!!!!!!!
    # if b in no_hear:
    #     no_list.append(b)
#리스트를 집합으로 만들어주고 교집합을 구한뒤 다시 리스트로 바꾼다.
no_list = list(set(no_hear) & set(no_see))
#사전순
no_list.sort()

print(len(no_list))
for i in range(len(no_list)):
    print(no_list[i])