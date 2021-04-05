import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    n, numbers = input().split()
    s = []

    for number in numbers:
        # 스택이 비어 있으면 우선 넣어주고 시작
        if not s:
            s.append(number)
        # 안비어 있으면 스택의 마지막 부분과 지금 들어오는 number가 똑같은지 확은해서
        else:
            # 똑같으면 지금 스택에 들어있는 값을 빼주고
            if s[-1] == number:
                s.pop()
            # 안 똑같으면 계속 넣어줌
            else:
                s.append(number)

    print("#{} {}".format(tc, "".join(map(str, s))))

