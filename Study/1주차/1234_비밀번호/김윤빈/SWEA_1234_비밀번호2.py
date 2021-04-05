import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N, password = input().split()
    password = list(password)
    # print(N,password)

    stack = []

    for i in range(len(password)):
        # 스택에 없으면 넣고
        if not stack:
            stack.append(password[i])
        # stack에 뭔가 있다

        elif stack[-1] == password[i]:
            stack.pop()
        else:
            stack.append(password[i])
    print("#{} {}".format(tc,''.join(map(str,stack))))