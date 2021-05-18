N = int(input())
# 방문 검사를 위한 변수
visited = 0
# 처음에 더할값 초기화
temp = 1
# 결과값 초기화
result = 1
# N만큼 규칙에 따라서 더해질 것이다.
for _ in range(N):
    # 만약 값이 짝수라면 바로 temp에서 더해준다.
    if not temp % 2:
        # 바로
        temp += 1
    else:
        # 홀수인 경우에는 두번 더해지므로 이미 한번 더해졌다면
        if visited:
            # 더할 값 증가
            temp += 1
            # 방문검사 초기화
            visited = 0
        else:
            # 더해진 적이 없다면 방문 체크만 하자
            visited = 1
    # 결과값에 더할값을 더해주자
    result += temp

print(result)