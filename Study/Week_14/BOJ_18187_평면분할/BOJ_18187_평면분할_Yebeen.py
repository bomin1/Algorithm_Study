N = int(input())
res = 2 #초기 n = 1일 때 분할 면은 2임
add = 2
cnt = 0 # cnt == N-1이 되면 끝
odd = False
while(cnt != N-1):
    res = res + add
    cnt += 1
    if odd == True: #더하는 값이 홀수일 때 두번 더해줬으니까 다음 더할 값에는 +=1헤주고 넘어감
        odd = False
        add += 1
        continue
    if add % 2 == 1: #더하는 값이 홀수이면 다음거에 +=1 안해줌
        odd = True # True로 바꿔주고
        continue
    add += 1 #더하는 값이 짝수이면 다음 더할 값에 +=1
print(res)