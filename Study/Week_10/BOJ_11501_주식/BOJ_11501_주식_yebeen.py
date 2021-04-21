T = int(input())
for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    lst.reverse() #거꾸로 보기
    M = lst[0]
    ans = 0
    for i in range(len(lst)):
        if M >= lst[i]:
            ans += M - lst[i]
        else:
            M = lst[i] # 큰게 있다면 최고가 갱신
    print(ans)