N = int(input())
line = list(map(int, input().split()))
cnt = 0
for i in range(N-1):
    if line[i] >= line[i+1]:
        print(i)
        cnt += 1
        continue
print(cnt)
# 증가할 때만 전깃줄이 꼬이지 않고
# 다음 수가 작거나 같으면 cnt++ 해주는 거였는데
#모르겠다
