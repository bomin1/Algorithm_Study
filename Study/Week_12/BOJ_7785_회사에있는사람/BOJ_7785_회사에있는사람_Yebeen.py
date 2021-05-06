n = int(input())
#딕셔너리로 받아서 value를 enter면 1을 넣고 leave면 0으로 바꾼다.
#최종으로 1이 있는 키 출력
room = {}
for tc in range(1,n+1):
    name,value = input().split()
    if value == 'enter':
        room[name] = 1
    else:
        room[name] = 0
res = []
for key,value in room.items():
    if value == 1:
        #사전 순의 역순으로 한 줄에 한 명씩 출력
        res.append(key)
res.sort(reverse=True)
for i in range(len(res)):
    print(res[i])
