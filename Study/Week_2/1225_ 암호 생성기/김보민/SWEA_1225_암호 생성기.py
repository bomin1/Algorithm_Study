import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    test = int(input())
    password = list(map(int, input().split()))
    minus = [-1,-2,-3,-4,-5]
    idx = 0

    while True:
        # 들어오는 입력값에서 제일 앞에 값 = check
        check = password.pop(0)
        # 마이너스의 0번째 인덱스에 접근해서 그 해당하는만큼 빼주고
        check += minus[idx]

        # 빼준 값이 음수이면
        if check <= 0:
            # 해당 값을 0으로 강제로 만들고
            check = 0
            # 맨 마지막에 추가하고 끝
            password.append(check)
            break
        # 빼준 값이 양수이면 그냥 뒤에 다시 추가해서 계속 진행
        password.append(check)

        # 마이너스 리스트에 접근하는 인덱스가 4가 되기전까지 +1해주면서 진행
        if idx != 4:
            idx += 1
        else:
            idx = 0

    print("#{} ".format(tc, ), end='')
    print(*password)

